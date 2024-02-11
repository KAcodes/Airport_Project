"""Backend API for use on Social News scraping site"""
from flask import Flask, jsonify, request
from flight_functions import (get_flights_from_iata, clean_flight_data, get_db_connection)
from dotenv import load_dotenv
from holiday_maker import generate_topic, format_ai_response, find_city_db

load_dotenv()
app = Flask(__name__)

# @app.route("/", methods=["GET"])
# def index():
#     """Gets stories page from html static file"""
#     return current_app.send_static_file("index.html")


@app.route("/departures/<iata>", methods=["GET"])
def countries(iata: str) -> dict:
    """Endpoint allows user to find flights departing from an airport"""
    print("checking")
    db_connection = get_db_connection()
    flights = get_flights_from_iata(iata)
    transformed_flights = clean_flight_data(flights, db_connection)
    response = jsonify(transformed_flights)
    
    return response


@app.route("/holiday_planner", methods=["POST"])
def make_holiday() -> dict:
    """Endpoint creates a holiday given specified details in input form"""

    holiday_details = request.json
    ai_response = generate_topic(holiday_details)
    formatted_response = format_ai_response(ai_response)
    return jsonify({
        "response": formatted_response
    })


@app.route('/cities/<query>', methods=['GET'])
def get_city_suggestions(query):
    
    db_connection = get_db_connection()
    suggestions = find_city_db(query, db_connection)
    return jsonify(suggestions)


if __name__ == "__main__":
    # app.run(debug=True, host="0.0.0.0", port=5000)
    app.run(debug=True)

