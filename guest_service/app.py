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
@app.route("/guests", methods=["GET", "POST"])
def guests():
    if request.method == "GET":
        query = "SELECT * FROM Guest ORDER BY guest_id DESC LIMIT 300"
        guests = execute_query(query)
        return jsonify(guests), 200

    elif request.method == "POST":
        data = request.get_json()
        full_name = data.get("full_name")
        country = data.get("country")
        email = data.get("email")

        query = """
            INSERT INTO Guest (full_name, country, email)
            VALUES (%s, %s, %s)
        """
        params = (full_name, country, email)
        result = execute_query(query, params, fetch=False)
        return jsonify(result), 201

# ---------------- MAIN ---------------- #
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003, debug=False)