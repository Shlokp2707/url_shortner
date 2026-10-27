import mysql.connector
import os
def get_connect():
    return mysql.connector.connect(
        host =os.getenv("host"),
        user =os.getenv("user"),
        password =os.getenv("password"),
        database =os.getenv("database")
    )
# def get_all_url():
#     conn =get_connect()
#     if conn.is_connected():
#         cursor =conn.cursor()
#         cursor.execute("Select url,id from url_table")
#         return cursor.fetchall()
def get_all_url():
    conn = get_connect()

    try:
        cursor = conn.cursor()
        cursor.execute("SELECT url, id FROM url_table")
        return cursor.fetchall()
    finally:
        cursor.close()
        conn.close()