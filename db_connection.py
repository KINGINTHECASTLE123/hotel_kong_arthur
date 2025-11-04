import os
import mysql.connector

DATABASE_CONFIG = {
    "host": os.getenv("DB_HOST", "db"),
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD", ""),
    "database": os.getenv("DB_NAME", "hotel_kong_arthur2"),
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