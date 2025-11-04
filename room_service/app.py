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
    "database": os.getenv("DB_NAME", "hotel_kong_arthur2"),
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
@app.route("/rooms", methods=["GET", "POST"])
def rooms():
    if request.method == "GET":
        query = "SELECT * FROM Room ORDER BY room_id"
        rooms = execute_query(query)
        return jsonify(rooms), 200

    elif request.method == "POST":
        data = request.get_json()
        query = """
            INSERT INTO Room (room_type, price_low, price_mid, price_high)
            VALUES (%s, %s, %s, %s)
        """
        params = (
            data.get("room_type"),
            data.get("price_low"),
            data.get("price_mid"),
            data.get("price_high")
        )
        result = execute_query(query, params, fetch=False)
        return jsonify(result), 201

@app.route("/rooms/<int:room_id>", methods=["PATCH"])
def update_room(room_id):
    data = request.get_json()
    query = """
        UPDATE Room
        SET price_low=%s, price_mid=%s, price_high=%s
        WHERE room_id=%s
    """
    params = (
        data.get("price_low"),
        data.get("price_mid"),
        data.get("price_high"),
        room_id
    )
    result = execute_query(query, params, fetch=False)
    return jsonify(result), 200

# ---------------- MAIN ---------------- #
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5004, debug=False)