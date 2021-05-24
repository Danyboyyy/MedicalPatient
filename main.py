import psycopg2
from psycopg2 import Error
from dotenv import load_dotenv
import os
import gui

load_dotenv()
USER = os.getenv('USER')
PSSWD = os.getenv('PSSWD')
HOST = os.getenv('HOST')
PORT = os.getenv('PORT')
DB = os.getenv('DB')

try:
  connection = psycopg2.connect(user=USER, password=PSSWD, host=HOST, port=PORT, database=DB)
  cursor = connection.cursor()
except (Exception, Error) as error:
  print("Error while connecting to PostgreSQL", error)
  exit()

gui.display(cursor)

if (connection):
  cursor.close()
  connection.close()
  print("PostgreSQL connection is closed")