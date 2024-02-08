"""This script cleans & builds upon the data collected from the Hacker News API."""
from datetime import datetime
from os import environ
import json
import logging

from dotenv import load_dotenv
import pandas as pd
import openai
from pandarallel import pandarallel
from psycopg2.extras import RealDictCursor
import psycopg2

from flight_functions import get_db_connection



load_dotenv()
VALID_TOPIC_IDS = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11")
client = openai.OpenAI(
    api_key=environ["OPENAI_API_KEY"]
)

pandarallel.initialize(progress_bar=True)


def handle_openai_errors(err):
    """OpenAI API request error-handling as per official docs."""
    if isinstance(err, openai.APIError):
        logging.exception("OpenAI API returned an API Error: %s", err)
    elif isinstance(err, openai.APIConnectionError):
        logging.exception("Failed to connect to OpenAI API: %s", err)
    elif isinstance(err, openai.RateLimitError):
        logging.exception("OpenAI API request exceeded rate limit: %s", err)
    else:
        logging.exception("Unexpected error: %s", err)

    raise err


def calculate_holiday_duration(date1, date2):
    d1 = datetime.strptime(date1, "%d/%m/%Y")
    d2 = datetime.strptime(date2, "%d/%m/%Y")
    day_difference = (d2 - d1).days
    return "a day trip" if day_difference == 0 else f"a {day_difference} night trip"


def find_city_db(searched_city, db_connection):
    with db_connection.cursor(cursor_factory=RealDictCursor) as cursor:
        try: 
            query = f"%{searched_city}%"
            cursor.execute(
                """SELECT city_id, city_name, countries.country_name FROM cities
                JOIN countries ON cities.country_id = countries.country_id
                WHERE city_name ILIKE %s""", (query,))
            rows = cursor.fetchall()
            return sorted(rows, key=lambda x: x["country_name"])
    
        except psycopg2.Error as e:
            print(f"Error executing SQL query: {e}")
            return ({"error": "Database query error"}), 500
        
        finally:
            cursor.close()
            db_connection.close()


def generate_topic(holiday_details: json) -> str:
    """Finds the most suitable topic for a url from a predefined list of topics 
    using the OpenAI API."""

    user_destination = holiday_details["location"]
    adults_number = holiday_details["adults"]
    children_number = holiday_details["children"]
    holiday_duration = calculate_holiday_duration(
        holiday_details["dept_date"], holiday_details["return_date"])

    system_content_spec = """
        You are a helpful assistant giving people travel ideas given their age,
        what country they are going and who they are with and how long they are there for.
        """
    user_content_spec = f"""I am planning a holiday for {adults_number} adults and {children_number} children,
    going to {user_destination}
    for {holiday_duration}. What is there to do?"""

    try:
        completion = client.chat.completions.create(
            model=environ["GPT-MODEL"],
            messages=[
                {"role": "system",
                    "content": system_content_spec},
                {"role": "user",
                    "content": user_content_spec}])
        return completion.choices[0].message.content
    except openai.APIError as error:
        return handle_openai_errors(error)
    

def format_ai_response(holiday: str) -> list[str]:
    holiday_ideas = holiday.split("\n")
    return [paragraph for paragraph in holiday_ideas if paragraph]


if __name__ == "__main__":
    conn = get_db_connection()
    find_city_db("Paris", conn)