import sqlite3 
import os 

# Set path of the Db to the current Working directory
path = os.path.dirname(os.path.abspath(__file__))

# Connect to database named MyDb.db
db = sqlite3.connect(f"{path}\\MyDb.db")

# Create a table that we will use in the Application
db.execute("create table if not exists Employees (Id integer PRIMARY KEY ,Name text, JobTitle text , Age integer , Salary integer)")