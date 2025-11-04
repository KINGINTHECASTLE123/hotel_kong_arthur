from flask import Flask, jsonify, request
from flask_cors import CORS
import os, mysql.connector

app = Flask(__name__)
CORS(app)

DATABASE_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD", ""),
    "database": os.getenv("DB_NAME", "hotel_kong_arthur2"),
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

@app.get("/guests")
def get_all_guests():
    return jsonify(execute_query("SELECT * FROM Guest ORDER BY guest_id DESC LIMIT 300"))

@app.post("/guests")
def create_guest():
    body = request.get_json()
    full_name = body["full_name"]
    country = body.get("country")
    email = body.get("email")
    result = execute_query(
        "INSERT INTO Guest (full_name, country, email) VALUES (%s, %s, %s)",
        (full_name, country, email),
        fetch_results=False
    )
    return jsonify(result), 201

if __name__ == "__main__":
    app.run(port=int(os.getenv("PORT", 5003)), host="0.0.0.0")