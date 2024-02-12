"""Backend API for use on Social News scraping site"""
from flask import Flask, jsonify, request
from dotenv import load_dotenv

from flight_functions import (
    get_flights_from_iata,
    transform_flight_data,
    get_db_connection
)
from holiday_maker import (
    generate_holiday,
    format_ai_response,
    find_city_suggestions,
    find_coordinates,
    find_nearest_hotels
)

load_dotenv()
app = Flask(__name__)


@app.route("/departures/<iata>", methods=["GET"])
def countries(iata: str) -> dict:
    """Endpoint allows user to find flights departing from an airport"""
    print("checking")
    db_connection = get_db_connection()
    flights = get_flights_from_iata(iata)
    transformed_flights = transform_flight_data(flights, db_connection)
    response = jsonify(transformed_flights)

    return response


@app.route("/holiday_planner", methods=["POST"])
def make_holiday() -> dict:
    """Endpoint creates a holiday given specified details in input form"""

    holiday_details = request.json
    ai_response = generate_holiday(holiday_details)
    formatted_response = format_ai_response(ai_response)

    return jsonify({
        "response": formatted_response
    })


@app.route('/cities/<query>', methods=['GET'])
def get_city_suggestions(query):
    """Endpoint returns all city suggestions as a list in which searched query
    matches city name in database"""

    db_connection = get_db_connection()
    suggestions = find_city_suggestions(query, db_connection)
    return jsonify(suggestions)


@app.route('/holiday_planner/hotels', methods=['POST'])
def find_hotels():
    """Endpoint returns hotels within a range of specified city"""

    db_connection = get_db_connection()
    holiday_details = request.json
    city_coordinates = find_coordinates(db_connection, holiday_details)
    nearest_hotels = find_nearest_hotels(city_coordinates, holiday_details)

    return jsonify({
        "api_response": nearest_hotels
    }), 200


if __name__ == "__main__":
    # app.run(debug=True, host="0.0.0.0", port=5000)
    app.run(debug=True)
