from flask import Flask, jsonify, request
from flask_cors import CORS
import os, mysql.connector

app = Flask(__name__)
CORS(app)

DATABASE_CONFIG = {
    "host": os.getenv("DB_HOST", "hotel_mysql_db"),
    "user": os.getenv("DB_USER", "hotel_user"),
    "password": os.getenv("DB_PASSWORD", "hotel_password"),
    "database": os.getenv("DB_NAME", "hotel_kong_arthur"),
}

def execute_query(sql, params=None, fetch_results=True):
    connection = mysql.connector.connect(**DATABASE_CONFIG)
    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql, params or ())
    if fetch_results:
        rows = cursor.fetchall()
    else:
        connection.commit()
        rows = {"rows_affected": cursor.rowcount, "last_insert_id": cursor.lastrowid}
    cursor.close(); connection.close()
    return rows

@app.get("/rooms")
def get_all_rooms():
    return jsonify(execute_query("SELECT * FROM Room ORDER BY room_id"))

@app.post("/rooms")
def create_room_type():
    body = request.get_json()
    room_type = body["room_type"]
    price_low = body.get("price_low")
    price_mid = body.get("price_mid")
    price_high = body.get("price_high")
    sql = "INSERT INTO Room (room_type, price_low, price_mid, price_high) VALUES (%s,%s,%s,%s)"
    result = execute_query(sql, (room_type, price_low, price_mid, price_high), fetch_results=False)
    return jsonify(result), 201

@app.patch("/rooms/<int:room_id>")
def update_room_prices(room_id):
    body = request.get_json()
    sql = "UPDATE Room SET price_low=%s, price_mid=%s, price_high=%s WHERE room_id=%s"
    result = execute_query(sql, (body.get("price_low"), body.get("price_mid"), body.get("price_high"), room_id), fetch_results=False)
    return jsonify(result)

if __name__ == "__main__":
    app.run(port=int(os.getenv("PORT", 5004)), host="0.0.0.0")