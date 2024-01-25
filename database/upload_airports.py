import json
from os import environ
import logging

import pandas as pd
import pycountry
import psycopg2
from dotenv import load_dotenv

countries = list(pycountry.countries)
ISO_COUNTRY_DICT = {country.alpha_2: country.name for country in countries}


load_dotenv()

def get_db_connection():
    """Returns a database connection."""
    try:
        connection = psycopg2.connect(
            host=environ["DB_HOST"],
            port=environ["DB_PORT"],
            database=environ["DB_NAME"],
            user=environ["DB_USER"],
        )
        return connection
    except psycopg2.OperationalError as error:
        # Log the specific error details for troubleshooting
        logging.exception("Error connecting to the database: %s", error)


def load_airport_JSON() -> list:
    """Load airport data from airports.json"""
    with open('airports.json', encoding="UTF-8") as data:
        airport_data = json.load(data)
    return airport_data


def clean_airports(airports: list):
    """Returns a cleaned dataframe"""

    df = pd.DataFrame.from_dict(airports)
    df = df[df["type"] == "airport"]
    df = df.drop(["size", "status", "type"] , axis=1)

    df['lat'] = pd.to_numeric(df['lat'], errors='coerce')
    df['lon'] = pd.to_numeric(df['lon'], errors='coerce')

    order = ['iata', 'name', 'iso', 'continent', 'lat',
             'lon']
    
    df = df[order]
    print(df)


def load_airports(df: pd.DataFrame, connection) -> None:
    """Gets stories and records data from dataframe. Uploads it to database tables.
    If story is already in story table then values are updated with latest version."""

    story_query = """
            INSERT INTO airports
                (iata, airport_name, iso, latitude, longitude)
            VALUES
                (%s, %s, %s, %s, %s)
            ON CONFLICT (story_id)
            DO UPDATE SET (title, author, story_url, creation_date, topic_id) = (EXCLUDED.title, EXCLUDED.author, EXCLUDED.story_url, EXCLUDED.creation_date, EXCLUDED.topic_id)
            ;
            """

    with connection.cursor() as cursor:
        stories_columns = df[["id", "title", "author",
                              "story_url", "creation_date", "topic_id"]]
        records_columns = df[["id", "score", "comments"]]

        stories_insert = stories_columns.values.tolist()
        records_insert = records_columns.values.tolist()

        # execute_values is a faster option if necessary, but you have to rework the query etc.
        cursor.executemany(
            story_query, stories_insert)


if __name__ == "__main__":
    airport_list = load_airport_JSON()
    clean_airports(airport_list)
    
# Display the resulting dictionary
