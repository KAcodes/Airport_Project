"""Backend API for use on Social News scraping site"""
from flask import Flask, current_app, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    """Gets stories page from html static file"""
    return current_app.send_static_file("index.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
