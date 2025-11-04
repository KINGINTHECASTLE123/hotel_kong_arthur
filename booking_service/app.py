from flask import Flask, jsonify, request
from flask_cors import CORS
import mysql.connector
import os

app = Flask(__name__)
CORS(app)

# ---------------- DATABASE CONFIG ---------------- #
DATABASE_CONFIG = {
    "host": os.getenv("DB_HOST", "db"),
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD", ""),
    "database": os.getenv("DB_NAME", "hotel_kong_arthur2")
}

# ---------------- HELPER FUNCTION ---------------- #
def execute_query(query, params=None, fetch=True):
    try:
        conn = mysql.connector.connect(**DATABASE_CONFIG)
        cursor = conn.cursor(dictionary=True)
        cursor.execute(query, params or ())

        if fetch:
            result = cursor.fetchall()
        else:
            conn.commit()
            result = {
                "rows_affected": cursor.rowcount,
                "last_insert_id": cursor.lastrowid
            }

        cursor.close()
        conn.close()
        return result

    except mysql.connector.Error as err:
        return {"error": str(err)}

# ---------------- ROUTES ---------------- #
@app.route("/bookings", methods=["GET", "POST"])
def bookings():
    if request.method == "GET":
        query = "SELECT * FROM Booking ORDER BY booking_id DESC LIMIT 200"
        bookings = execute_query(query)
        return jsonify(bookings), 200

    elif request.method == "POST":
        data = request.get_json()
        query = """
            INSERT INTO Booking (guest_id, room_id, season, days_rented, total_price)
            VALUES (%s, %s, %s, %s, %s)
        """
        params = (
            data.get("guest_id"),
            data.get("room_id"),
            data.get("season"),
            data.get("days_rented"),
            data.get("total_price")
        )
        result = execute_query(query, params, fetch=False)
        return jsonify(result), 201

# ---------------- MAIN ---------------- #
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=False)