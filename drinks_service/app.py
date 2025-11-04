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
@app.route("/drinks", methods=["GET", "POST"])
def drinks():
    if request.method == "GET":
        query = "SELECT * FROM DrinkSale ORDER BY sale_id DESC LIMIT 300"
        drinks = execute_query(query)
        return jsonify(drinks), 200

    elif request.method == "POST":
        data = request.get_json()
        drink_name = data.get("drink_name")
        category = data.get("category")
        price = float(data.get("price", 0))
        units_sold = int(data.get("units_sold", 0))
        total_sale = data.get("total_sale", price * units_sold)

        query = """
            INSERT INTO DrinkSale (drink_name, category, price, units_sold, total_sale)
            VALUES (%s, %s, %s, %s, %s)
        """
        params = (drink_name, category, price, units_sold, total_sale)
        result = execute_query(query, params, fetch=False)
        return jsonify(result), 201

@app.route("/drinks/kpi/category", methods=["GET"])
def kpi_by_category():
    query = "SELECT * FROM v_drink_revenue_by_category"
    result = execute_query(query)
    return jsonify(result), 200

@app.route("/drinks/kpi/top", methods=["GET"])
def kpi_top_drinks():
    query = "SELECT * FROM v_drinks_aggregated ORDER BY revenue DESC LIMIT 50"
    result = execute_query(query)
    return jsonify(result), 200

# ---------------- MAIN ---------------- #
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=False)