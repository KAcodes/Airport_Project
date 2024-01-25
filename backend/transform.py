"""This script cleans & builds upon the data collected from the Hacker News API."""
from os import environ
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


# def generate_topic(story_url: str) -> str:
#     """Finds the most suitable topic for a url from a predefined list of topics 
#     using the OpenAI API."""

#     system_content_spec = """
#         You are a classifying bot that can categorise titles into only these categories by returning the corresponding number:
#             1. Programming & Software Development
#             2. Game Development
#             3. Algorithms & Data Structures
#             4. Web Development & Browser Technologies
#             5. Computer Graphics & Image Processing
#             6. Operating Systems & Low-level Programming
#             7. Science & Research Publications
#             8. Literature & Book Reviews
#             9. Artificial Intelligence & Machine Learning
#             10. News & Current Affairs.
#             11. Miscellaneous & Interesting Facts"""
#     user_content_spec = f"""
#         Categorise this title into one of the listed categories: {story_url}.
#         Only state the category number and nothing else. Ensure your only output is a number."""

#     try:
#         completion = client.chat.completions.create(
#             model=environ["GPT-MODEL"],
#             messages=[
#                 {"role": "system",
#                     "content": system_content_spec},
#                 {"role": "user",
#                     "content": user_content_spec}])
#         return completion.choices[0].message.content
#     except openai.APIError as error:
#         return handle_openai_errors(error)

def generate_topic(story_url: str) -> str:
    """Finds the most suitable topic for a url from a predefined list of topics 
    using the OpenAI API."""

    system_content_spec = """
        You are a helpful assistant giving people travel ideas given their age, what country they are going and who they are with and how long they are there for."""
    user_content_spec = f"""
        I am a 25-year-old male, going to Paris by myself for two days 12th-14th July 2024. What is there to do?"""

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


if __name__ == "__main__":

    print(generate_topic("React is no longer the best."))