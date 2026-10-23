import tkinter as tk
from tkinter import messagebox
import sqlite3

connection=sqlite3.connect("student.db")
cursor=connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
     student_id INTEGER PRIMARY KEY,
     name TEXT,
     course TEXT,
     email TEXT
)
""")

connection.commit()

#GUI

root =tk.Tk()
root.title("Student Management System")
root.geometry("500x500")
root.resizable(False,False)

root.mainloop()
