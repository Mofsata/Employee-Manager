import sqlite3 
import os 

path = os.path.dirname(os.path.abspath(__file__))
db = sqlite3.connect(f"{path}\\MyDb.db")
db.execute("create table if not exists Employees (Id integer PRIMARY KEY ,Name text, JobTitle text , Age integer , Salary integer)")