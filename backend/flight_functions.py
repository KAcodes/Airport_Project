"""Functions for """
import json
from os import environ
import logging
import requests

import pandas as pd
import psycopg2
from psycopg2.extensions import connection
from dotenv import load_dotenv

AIRLABS_API_URL = "https://airlabs.co/api/v9/schedules"

load_dotenv()

def get_db_connection() -> connection:
    """Returns a database connection."""
    try:
        conn = psycopg2.connect(
            host=environ["DB_HOST"],
            port=environ["DB_PORT"],
            database=environ["DB_NAME"],
            user=environ["DB_USER"],
        )
        return conn
    except psycopg2.OperationalError as error:
        # Log the specific error details for troubleshooting
        logging.exception("Error connecting to the database: %s", error)


def get_flights_from_iata(iata: str) -> list:
    """Given an IATA get the flights that are departing from that airport from Airlabs"""
    response = requests.get(
        f"{AIRLABS_API_URL}?dep_iata={iata}&api_key={environ['AIRLABS_API_KEY']}", timeout=60)
    return response.json()["response"]


def calculate_flight_hours(duration: int) -> str:
    hours = duration//60
    mins = duration % 60
    if len(str(mins)) == 1:
        return f"{hours}:{mins}0"
    return f"{hours}:{mins}"


def calculate_flight_hours(duration: int) -> str:
    hours = duration//60
    mins = duration % 60
    if len(str(mins)) == 1:
        return f"{hours}h:{mins}0m"
    return f"{hours}h:{mins}m"

def clean_flight_data(flight_departures: list, db_connection: connection):

    dept_list = []
    for departure in flight_departures:

        relevant_cols = ["flight_iata", "dep_time_utc", "arr_iata", "arr_time_utc",
                         "duration"]
        departure = {col: departure.get(col) for col in relevant_cols}
        dept_list.append(departure)

    sorted_dept = sorted(dept_list, key=lambda x: x['dep_time_utc'])
    
    transformed_flights = []
    with db_connection.cursor() as cursor:
        
        for flight in sorted_dept:

            country_id_query = f"""SELECT airport_name, countries.country_name FROM airports
                                JOIN countries ON airports.country_id = countries.country_id
                                WHERE iata LIKE '{flight["arr_iata"]}';"""
            cursor.execute(country_id_query)

            airport_info = cursor.fetchone()
            if airport_info is None:
                continue
            flight["destination_airport"], flight["destination_country"] = airport_info[0], airport_info[1]
            flight["duration"] = calculate_flight_hours(flight["duration"])
            transformed_flights.append(flight)

    return transformed_flights
