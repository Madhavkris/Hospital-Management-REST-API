from flask_sqlalchemy import SQLAlchemy
db=SQLAlchemy()

"""
import mysql.connector
import os
from dotenv import load_dotenv
load_dotenv()
def get_connect():
    try:
        connection=mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_DATABASE"))

        return connection
    except mysql.connector.Error as err:
        print("Database connection failed",err)
        return None
"""
