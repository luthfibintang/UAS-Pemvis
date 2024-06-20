from connection import create_connection
from mysql.connector import Error

def check_credentials(email, password):
    connection = create_connection()
    if connection:
        cursor = connection.cursor(dictionary=True)
        query = "SELECT id, role FROM users WHERE email = %s AND password = %s"
        cursor.execute(query, (email, password))
        user = cursor.fetchone()
        cursor.close()
        connection.close()
        if user:
            return user
    return None

def register_user(nik, name, email, password, phone):
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        query = "INSERT INTO users (nik, nama, email, password, telp) VALUES (%s, %s, %s, %s, %s)"
        try:
            cursor.execute(query, (nik, name, email, password, phone))
            connection.commit()
            return True
        except Error as e:
            print(f"Error: {e}")
            return False
        finally:
            cursor.close()
            connection.close()
    return False