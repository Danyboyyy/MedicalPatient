import psycopg2
from psycopg2 import Error
import tkinter as tk
from dotenv import load_dotenv
import os

load_dotenv()
USER = os.getenv('USER')
PSSWD = os.getenv('PSSWD')
HOST = os.getenv('HOST')
PORT = os.getenv('PORT')
DB = os.getenv('DB')


window = tk.Tk()
window.geometry("400x300")
title = tk.Label(window, text = "MedicalPatient")
title.pack(fill = tk.X)

try:
  connection = psycopg2.connect(user=USER, password=PSSWD, host=HOST, port=PORT, database=DB)
  cursor = connection.cursor()
  cursor.execute("SELECT * FROM person")
  result = cursor.fetchall()
  print(result)
except (Exception, Error) as error:
  print("Error while connecting to PostgreSQL", error)
  exit()

window.mainloop()

if (connection):
  cursor.close()
  connection.close()
  print("PostgreSQL connection is closed")