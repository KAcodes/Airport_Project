"""Backend API for use on Social News scraping site"""
from flask import Flask, request

app = Flask(__name__)

# @app.route("/", methods=["GET"])
# def index():
#     """Gets stories page from html static file"""
#     return current_app.send_static_file("index.html")


@app.route("/countries/<country>", methods=["GET"])
def countries(country: str) -> dict:
    """Endpoint allows user to delete story of their choice"""
    return {
        "results": f"Name of your country: {country}"
    }



if __name__ == "__main__":
    # app.run(debug=True, host="0.0.0.0", port=5000)
    app.run(debug=True)

