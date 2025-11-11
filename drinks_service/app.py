from flask import Flask, jsonify, request
from flask_cors import CORS
import os, mysql.connector

app = Flask(__name__)
CORS(app)

# ----- Database config -----
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

# ----- Endpoints -----
@app.get("/drinks")
def get_all_drink_sales():
    return jsonify(execute_query("SELECT * FROM DrinkSale ORDER BY sale_id DESC LIMIT 300"))

@app.post("/drinks")
def create_drink_sale():
    body = request.get_json()
    drink_name = body["drink_name"]
    category = body["category"]
    price = int(body["price"])
    units_sold = int(body["units_sold"])
    total_sale = body.get("total_sale", price * units_sold)

    sql = """INSERT INTO DrinkSale (drink_name, category, price, units_sold, total_sale)
             VALUES (%s, %s, %s, %s, %s)"""
    result = execute_query(sql, (drink_name, category, price, units_sold, total_sale), fetch_results=False)
    return jsonify(result), 201

# KPI/aggregater (matchende views du allerede har oprettet)
@app.get("/drinks/kpi/category")
def kpi_drinks_by_category():
    return jsonify(execute_query("SELECT * FROM v_drink_revenue_by_category"))

@app.get("/drinks/kpi/top")
def kpi_top_drinks():
    return jsonify(execute_query("SELECT * FROM v_drinks_aggregated ORDER BY revenue DESC LIMIT 50"))

if __name__ == "__main__":
    app.run(port=int(os.getenv("PORT", 5002)), host="0.0.0.0")