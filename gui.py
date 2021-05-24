from tkinter import ttk
import tkinter as tk
import queries

name = ["Person"]

def config(attributes, table):
  name.pop()

  if table == "Person":
    attributes["values"] = ["*", "pId", "firstName", "lastName", "dob", "gender"]
    name.append("Person")
  elif table == "Patient":
    attributes["values"] = ["*", "insurancePlan"]
    name.append("Patient")
  elif table == "Treatment":
    name["values"] = ["*", "duration", "medicaments", "description"]
    name.append("Treatment")
  elif table == "Doctor":
    attributes["values"] = ["*", "speciality", "yearsExperience"]
    name.append("Doctor")
  elif table == "Area":
    attributes["values"] = ["*", "name", "location"]
    name.append("Area")

def display(cursor):
  window = tk.Tk()
  window.title("MedicalPatient")

  attributes = ttk.Combobox(window, state = "readonly")

  btnPerson = tk.Button(window, text = "Person", command = lambda: config(attributes, "Person"), width = 20)
  btnPatient = tk.Button(window, text = "Patient", command = lambda: config(attributes, "Patient"), width = 20)
  btnTreatment = tk.Button(window, text = "Treatment", command = lambda: config(attributes, "Treatment"), width = 20)
  btnDoctor = tk.Button(window, text = "Doctor", command = lambda: config(attributes, "Doctor"), width = 20)
  btnArea = tk.Button(window, text = "Area", command = lambda: config(attributes, "Area"), width = 20)

  btnSelect = tk.Button(window, text = "Select", command = lambda: queries.select(cursor, attributes, name[0], results))

  results = tk.Text(window)

  btnPerson.grid(row = 0, column = 0, sticky = tk.E + tk.W)
  btnPatient.grid(row = 0, column = 1, sticky = tk.E + tk.W)
  btnTreatment.grid(row = 0, column  = 2, sticky = tk.E + tk.W)
  btnDoctor.grid(row = 0, column = 3, sticky = tk.E + tk.W)
  btnArea.grid(row = 0, column = 4, sticky = tk.E + tk.W)

  attributes.grid(row = 1, column = 0, sticky = tk.E + tk.W, pady = 20)
  btnSelect.grid(row = 2, column = 0, sticky = tk.E + tk.W)

  results.grid(row = 3, column = 0, columnspan=5, pady = 20)

  window.mainloop()