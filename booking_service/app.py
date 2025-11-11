## Med hjælp fra chatten: 

from flask import Flask, jsonify, request
from flask_cors import CORS
import os, mysql.connector

app = Flask(__name__)
CORS(app)

# Database config
DATABASE_CONFIG = {
    "host": os.getenv("DB_HOST", "mysql_db"),
    "user": os.getenv("DB_USER", "hotel_user"),
    "password": os.getenv("DB_PASSWORD", "hotel_password"),
    "database": os.getenv("DB_NAME", "hotel_kong_arthur"),
}

def execute_query(sql, params=None, fetch_results=True):
    connection = mysql.connector.connect(**DATABASE_CONFIG)
    cursor = connection.cursor(dictionary=True)
    
    cursor.execute(sql, params or ())
    
    if fetch_results:
        results = cursor.fetchall()
    else:
        connection.commit()
        results = {"rows_affected": cursor.rowcount, "last_insert_id": cursor.lastrowid}

    cursor.close()
    connection.close()
    return results

@app.get("/bookings")
def get_all_bookings():
    query = "SELECT * FROM Booking ORDER BY booking_id DESC LIMIT 200"
    bookings = execute_query(query)
    return jsonify(bookings)

@app.post("/bookings")
def create_booking():
    booking_data = request.get_json()
    
    query = """
        INSERT INTO Booking (guest_id, room_id, season, days_rented, total_price)
        VALUES (%s, %s, %s, %s, %s)
    """
    params = (
        booking_data["guest_id"],
        booking_data["room_id"],
        booking_data["season"],
        booking_data["days_rented"],
        booking_data["total_price"]
    )
    
    result = execute_query(query, params, fetch_results=False)
    return jsonify(result), 201

if __name__ == "__main__":
    app.run(port=5001, host="0.0.0.0")
