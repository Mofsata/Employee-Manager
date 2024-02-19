from flask import Flask ,request , jsonify
import sqlite3
import os



app = Flask(__name__)

# Jsonify function messes up the sorting of the dicts so we set the sorting off
app.json.sort_keys = False


def Db_connection() :
    conn = None
    try :
        path = os.path.dirname(os.path.abspath(__file__))
        conn = sqlite3.connect(f"{path}\\MyDb.db")
    except sqlite3.Error as e :
        print(e)
    return conn


@app.route("/" , methods = ['GET' , 'POST'])
def GetPostMethod() :
    db = Db_connection()
    cr = db.cursor()
    if request.method == 'GET' :
        cr.execute("select * from Employees")
        Employees = [
            dict(Id = row[0] , Name = row[1] , JobTitle = row[2] , Age = row[3] , Salary = row[4])
            for row in cr.fetchall()
        ]
        if Employees is not None : return jsonify(Employees)

    # get request from body (raw)
    if request.method == 'POST' :
        content = request.get_json(force=True)
        EmpName = content["Name"]
        EmpJobTitle = content["JobTitle"]
        EmpAge = content["Age"]
        EmpSalary = content["Salary"]

        sql = """Insert into Employees (Name , JobTitle, Age , Salary) values (?,?,?,?)"""
        cr.execute(sql , (EmpName, EmpJobTitle , EmpAge , EmpSalary))
        db.commit()
        
        return f"Employee with the id : {cr.lastrowid} created successfully" 
    
@app.route("/<int:id>" , methods = ['GET' , 'PUT' , 'DELETE'])
def IdMethods(id) :

    db = Db_connection()
    cr = db.cursor()

    if request.method == 'GET' :
        cr.execute(f"select * from Employees where Id = '{id}'")
        rows = cr.fetchall()
        emp = None
        for row in rows :
            emp = dict(Id = row[0] , Name = row[1] , JobTitle = row[2] , Age = row[3] , Salary = row[4])
        if emp == None : return "ID Not found"
        return jsonify(emp)


    
    if request.method == 'PUT' :

        sql_update = """update Employees Set Name = ? , JobTitle = ? , Age = ? , Salary = ? where Id = ? """

        # Get request from form
        EmpName = request.form["Name"]
        EmpJobTitle = request.form["JobTitle"]
        EmpAge = int(request.form["Age"])
        EmpSalary = int(request.form["Salary"])
        EmpUpdate = {
            "ID" : id,
            "Name" : EmpName,
            "JobTitle" : EmpJobTitle,
            "Age" : EmpAge ,
            "Salary" : EmpSalary
        }
        cr.execute(sql_update , (EmpName, EmpJobTitle , EmpAge , EmpSalary , id))
        db.commit()
        return jsonify(EmpUpdate)
    
    if request.method == 'DELETE' :
        sql_delete = """delete from Employees where Id = ? """
        cr.execute(sql_delete , (id,))
        db.commit()
        return f"the book with id = {id} has been deleted"


if __name__ == "__main__" :
    app.run(debug=True , port= 9000)
