from tkinter import *
from psycopg2.extensions import AsIs

def select(cursor, attributes, tableName, results):
  attr = attributes.get()

  cursor.execute("""SELECT %s FROM %s""", (AsIs(attr), AsIs(tableName)))

  result = cursor.fetchall()

  results.delete('1.0', END)
  for row in result:
    results.insert(END, row)
    results.insert(END, "\n")
  print(result)