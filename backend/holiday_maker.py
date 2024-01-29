"""This script cleans & builds upon the data collected from the Hacker News API."""
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


def generate_topic(holiday_details: json) -> str:
    """Finds the most suitable topic for a url from a predefined list of topics 
    using the OpenAI API."""

    user_age = holiday_details["age"]
    user_gender = holiday_details["gender"]
    user_destination = holiday_details["destination"]
    holiday_duration = holiday_details["duration"]


    system_content_spec = """
        You are a helpful assistant giving people travel ideas given their age,
        what country they are going and who they are with and how long they are there for.
        Specify each day with a number"""
    user_content_spec = f"""I am a {user_age} {user_gender}, going to {user_destination} by myself 
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


