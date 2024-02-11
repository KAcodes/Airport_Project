"""This script cleans & builds upon the data collected from the Hacker News API."""
from datetime import datetime
from os import environ
import json
import logging
import requests
import pandas as pd

from dotenv import load_dotenv
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
            query = f"{searched_city}%"
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


def find_coordinates(db_connection, city_id):
    with db_connection.cursor() as cursor:
        try:
            cursor.execute(
                f"""SELECT latitude, longitude FROM cities
                WHERE city_id = {city_id};""")
            coordinates = cursor.fetchone()
            return coordinates

        except psycopg2.Error as e:
            print(f"Error executing SQL query: {e}")
            return ({"error": "Database query error"}), 500

        finally:
            cursor.close()


def find_nearest_hotels(coordinates: tuple[str]):

    XRapidAPIHost = "priceline-com-provider.p.rapidapi.com"

    coordinates_url = f"https://{XRapidAPIHost}/v1/hotels/locations-by-geo"

    headers = {
        "X-RapidAPI-Key": environ["X-RAPIDAPI-KEY"],
        "X-RapidAPI-Host": XRapidAPIHost
    }

    coordinates_querystring = {"latitude": coordinates[0], "longitude": coordinates[1]}

    city_response = requests.get(
        coordinates_url, headers=headers, params=coordinates_querystring)

    city_result = city_response.json()
    if not city_result.get("matchedCity"):
        return
    
    cityID = city_result["matchedCity"]["cityID"]
    print(cityID)
    

    hotel_search_url = f"https://{XRapidAPIHost}/v1/hotels/search"

    hotel_querystring = {
        "location_id": cityID,
        "date_checkin": "2024-07-24",
        "date_checkout": "2024-07-25",
        "sort_order": "HDR",
        "star_rating_ids": "3.0,3.5,4.0,4.5,5.0",
        # potential options
        # "rooms_number": "1",
        # "amenities_ids": "FINTRNT,FBRKFST"
    }

    hotel_response = requests.get(
        hotel_search_url, headers=headers, params=hotel_querystring)

    hotels = pd.DataFrame(hotel_response.json()["hotels"])
    hotels.to_csv('hotels.csv', index=False)



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
    city_coordinates = find_coordinates(conn, 2643743)
    find_nearest_hotels(city_coordinates)
