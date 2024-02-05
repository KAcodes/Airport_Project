"""This script cleans & builds upon the data collected from the Hacker News API."""
from datetime import datetime
from os import environ
import json
import psycopg2
import logging
from dotenv import load_dotenv
import pandas as pd
import openai
from pandarallel import pandarallel

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


print(format_ai_response("""
For a group of adults traveling to Paris for a 3-night trip, there are plenty of cultural, historical, and entertainment options to consider. Here are a few ideas depending on your interests:

1. Visit iconic landmarks like the Eiffel Tower, Louvre Museum, Notre-Dame Cathedral, and Arc de Triomphe.
2. Explore the charming neighborhoods of Montmartre and Le Marais, known for their artistic and bohemian vibes.
3. Enjoy a scenic Seine River cruise to take in the city's landmarks from a different perspective.
4. Indulge in French cuisine at local bistros, cafes, and restaurants. Don't miss out on trying authentic French pastries and desserts.
5. Take a day trip to the Palace of Versailles, just outside of Paris, to experience opulent royal history and beautiful gardens.

Additionally, consider checking out any special events, exhibitions, or performances happening during your visit. Paris is known for its vibrant arts and cultural scene.

Always ensure to check the latest travel advisories and local guidelines during your trip. Have a fantastic time in the City of Light!
"""))
