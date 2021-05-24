import tkinter as tk

def display():
  window = tk.Tk()
  window.geometry("400x300")
  title = tk.Label(window, text = "MedicalPatient")
  title.pack(fill = tk.X)
  window.mainloop()