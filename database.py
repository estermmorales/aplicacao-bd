from dotenv import load_dotenv
import mysql.connector as conn
import os

load_dotenv()
mydb = conn.connect(
    host="localhost",
    user=os.getenv("user"),
    password=os.getenv("password"),
    database=os.getenv("database")
) 