from connection import get_db_connection
from mysql.connector import Error

def authenticate_user(email, password):
    connection = get_db_connection()
    if connection:
        try:
            cursor = connection.cursor()
            query = "SELECT * FROM users WHERE email=%s AND password=%s"
            cursor.execute(query, (email, password))
            user = cursor.fetchone()
            connection.close()
            return user
        except Error as e:
            print(f"Error: {e}")
            return None
    else:
        return None

def register_user(email, password):
    connection = get_db_connection()
    if connection:
        try:
            cursor = connection.cursor()
            query = "INSERT INTO users (email, password) VALUES (%s, %s)"
            cursor.execute(query, (email, password))
            connection.commit()
            connection.close()
            return True
        except Error as e:
            print(f"Error: {e}")
            return False
    else:
        return False
