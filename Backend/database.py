import pymysql
from config import *

def get_connection():
    print("PASSWORD =", DB_PASSWORD)
    return pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        autocommit=True
    )