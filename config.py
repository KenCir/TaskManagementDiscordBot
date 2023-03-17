import os
from dotenv import load_dotenv

load_dotenv()

MYSQL_USER = os.getenv('DB_USER')
MYSQL_PASSWORD = os.getenv('PASSWORD')
MYSQL_HOST = os.getenv('HOST')
MYSQL_DATABASE = os.getenv('DATABASE')
