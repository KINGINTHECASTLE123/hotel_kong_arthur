from flask import Flask, jsonify, request
from flask_cors import CORS
import os, mysql.connector

app = Flask(__name__)
CORS(app)

# Database configuration (læser fra .env via docker-compose)
DATABASE_CONFIG = {
    "host": os.getenv("DB_HOST", "hotel_mysql_db"),
    "user": os.getenv("DB_USER", "hotel_user"),
    "password": os.getenv("DB_PASSWORD", "hotel_password"),
    "database": os.getenv("DB_NAME", "hotel_kong_arthur"),
}

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

@app.get("/bookings")
def get_all_bookings():
    query = "SELECT * FROM Booking ORDER BY booking_id DESC LIMIT 200"
    bookings = execute_query(query)
    return jsonify(bookings)

@app.post("/bookings")
def create_booking():
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

# ---------------------------------------- #
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)