"""This script seeds the airports and countries tables within the PostgreSQL database"""
import json
from os import environ
import logging

import pandas as pd
import pycountry
import psycopg2
from psycopg2.extensions import connection
from dotenv import load_dotenv

all_countries = list(pycountry.countries)
ISO_COUNTRY_DICT = {country.alpha_2: country.name for country in all_countries}

load_dotenv()

def get_db_connection() -> connection:
    """Returns a database connection."""
    try:
        conn = psycopg2.connect(
            host=environ["DB_HOST"],
            port=environ["DB_PORT"],
            database=environ["DB_NAME"],
            user=environ["DB_USER"],
            password=environ["DB_PASSWORD"]
        )
        return conn
    except psycopg2.OperationalError as error:
        # Log the specific error details for troubleshooting
        logging.exception("Error connecting to the database: %s", error)


def load_json(file_name) -> list:
    """Load airport data from airports.json"""
    with open(f'{file_name}.json', encoding="UTF-8") as data:
        json_data = json.load(data)
    return json_data


def clean_airports(airports: list) -> pd.DataFrame:
    """Returns a dataframe of all airports cleaned from NaN values and formatted to enter db"""

    df = pd.DataFrame.from_dict(airports)
    df = df[df["type"] == "airport"]
    df = df.drop(["size", "status", "type"] , axis=1)
    df['country'] = df['iso'].apply(lambda x: ISO_COUNTRY_DICT.get(x))

    df['lat'] = pd.to_numeric(df['lat'], errors='coerce')
    df['lon'] = pd.to_numeric(df['lon'], errors='coerce')

    df = df.dropna()
    order = ['iata', 'name', 'iso', 'country', 'continent', 'lat', 'lon']
    df = df[order]

    return df


def clean_cities(cities: list) -> pd.DataFrame:
    """Returns a dataframe of all airports cleaned from NaN values and formatted to enter db"""

    df = pd.DataFrame.from_dict(cities)
    df = df.drop(["pop", "admin1"], axis=1)

    df['lat'] = pd.to_numeric(df['lat'], errors='coerce')
    df['lon'] = pd.to_numeric(df['lon'], errors='coerce')

    return df


def populate_country_table(airports: pd.DataFrame, db_connection: connection):
    """Populates countries table in PostgreSQL database from airport dataframe"""

    countries = airports[['iso', 'country', 'continent']]
    countries = countries.drop_duplicates(subset='iso')
    countries = countries.sort_values("country")

    countries_insert = countries.values.tolist()
    country_query = """
            INSERT INTO countries
                (iso, country_name, continent)
            VALUES
                (%s, %s, %s);
            """

    with db_connection.cursor() as cursor:

        cursor.executemany(
            country_query, countries_insert)
        db_connection.commit()


def populate_cities_table(cities_df: pd.DataFrame, db_connection: connection):
    """Populates countries table in PostgreSQL database from airport dataframe"""

    cities = cities_df.sort_values("name")

    cities_data = cities.values.tolist()
    cities_query = """
            INSERT INTO cities
                (city_id, city_name, country_id, latitude, longitude)
            VALUES
                (%s, %s, %s, %s, %s);
            """

    cities_insert = []
    with db_connection.cursor() as cursor:

        for city in cities_data:

            country_id_query = f"""SELECT country_id FROM countries
                        WHERE iso LIKE '{city[2]}';"""
            cursor.execute(country_id_query)
            iso_check = cursor.fetchone()
            if iso_check is not None:
                city[2] = iso_check[0]
                cities_insert.append(city)

        cursor.executemany(
            cities_query, cities_insert)
        db_connection.commit()


def populate_airports(airport_df: pd.DataFrame, db_connection: connection) -> None:
    """Populates airports table in PostgreSQL database,
    finds country id from comparing iso with countries table"""

    airport_df = airport_df.sort_values("name")
    airport_data = airport_df[['iata', 'name', 'iso', 'lat',
                                'lon']].values.tolist()

    with db_connection.cursor() as cursor:

        for airport in airport_data:

            country_id_query = f"""SELECT country_id FROM countries
                        WHERE iso LIKE '{airport[2]}';"""
            cursor.execute(country_id_query)
            airport[2] = cursor.fetchone()[0]

        airport_query = """
            INSERT INTO airports
                (iata, airport_name, country_id, latitude, longitude)
            VALUES
                (%s, %s, %s, %s, %s);
            """

        cursor.executemany(airport_query, airport_data)
        db_connection.commit()


if __name__ == "__main__":
    cities_list = load_json("cities")
    cleaned_cities = clean_cities(cities_list)
    # airport_list = load_json("airports")
    # cleaned_airports = clean_airports(airport_list)
    db_conn = get_db_connection()
    # populate_country_table(cleaned_airports, db_conn)
    # populate_airports(cleaned_airports, db_conn)
    populate_cities_table(cleaned_cities, db_conn)
