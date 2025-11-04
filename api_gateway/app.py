from flask import Flask, jsonify, request
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)

# ---------------- CONFIG ---------------- #
SERVICE_URLS = {
    "booking_service": os.getenv("BOOKING_SERVICE_URL", "http://localhost:5001"),
    "drinks_service":  os.getenv("DRINKS_SERVICE_URL",  "http://localhost:5002"),
    "guest_service":   os.getenv("GUEST_SERVICE_URL",   "http://localhost:5003"),
    "room_service":    os.getenv("ROOM_SERVICE_URL",    "http://localhost:5004"),
}

# ---------------- HELPER ---------------- #
def forward_to_service(method, url, json_data=None):
    """Sender request videre til en microservice."""
    try:
        response = requests.request(method, url, json=json_data, timeout=5)
        response.raise_for_status()
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Service unavailable: {str(e)}"}), 503

# ---------------- ROUTES ---------------- #
@app.route("/api/bookings", methods=["GET", "POST"])
def bookings():
    service_url = f"{SERVICE_URLS['booking_service']}/bookings"
    if request.method == "GET":
        return forward_to_service("GET", service_url)
    elif request.method == "POST":
        return forward_to_service("POST", service_url, json_data=request.get_json())

@app.route("/api/drinks", methods=["GET"])
def drinks():
    return forward_to_service("GET", f"{SERVICE_URLS['drinks_service']}/drinks")

@app.route("/api/guests", methods=["GET"])
def guests():
    return forward_to_service("GET", f"{SERVICE_URLS['guest_service']}/guests")

@app.route("/api/rooms", methods=["GET"])
def rooms():
    return forward_to_service("GET", f"{SERVICE_URLS['room_service']}/rooms")

# ---------------- MAIN ---------------- #
if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=os.getenv("FLASK_DEBUG", "false").lower() == "true"
    )