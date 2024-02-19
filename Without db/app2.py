from flask import Flask , request , jsonify

app = Flask(__name__)

Employees_List = [
                    {
                        "ID" : 0,
                        "Name" : "Mostafa Ahmed" ,
                        "JobTitle" : "DevOps Engineer",
                        "Salary" : "8000"
                    },
                    {
                        "ID" : 1,
                        "Name" : "Mostafa Amin" ,
                        "JobTitle" : "System Admin",
                        "Salary" : "10000"
                    },
                    {
                        "ID" : 2,
                        "Name" : "Moaz Mohammed" ,
                        "JobTitle" : "AIO Developer",
                        "Salary" : "20000"
                    }
                   ]



@app.route("/" , methods = ['GET' , 'POST'])
def Employees() :
    if request.method == 'GET' :
        return jsonify(Employees_List)
    
    if request.method == 'POST' :
        EmpName = request.form["Name"]
        EmpJobTitle = request.form["JobTitle"]
        EmpSalary = request.form["Salary"]

        EmpID = Employees_List[-1]["ID"]+1
        NewEmp = {
                    "ID" : EmpID,
                    "Name" : EmpName ,
                    "JobTitle" : EmpJobTitle,
                    "Salary" : EmpSalary
                }
        
        Employees_List.append(NewEmp)

        return jsonify(Employees_List) 




@app.route("/id/<int:id>" , methods = ['GET' ,'PUT' , 'DELETE'])
def EmpID(id) :
    if request.method == 'GET' :
        for emp in Employees_List :
            if emp["ID"] == id :
                return jsonify(emp)
        return "ID Not Found"

    if request.method == 'PUT' :
        for emp in Employees_List :
                if emp["ID"] == id :
                    emp["Name"] = request.form["Name"]
                    emp["JobTitle"] = request.form["JobTitle"]
                    emp["Salary"] = request.form["Salary"]

                    return jsonify(emp)
        return "ID Not Found"

    if request.method == 'DELETE' :
        for emp in Employees_List :
            if emp["ID"] == id :
                Employees_List.remove(emp)
                return jsonify(Employees_List)
        return "ID Not Found"

if __name__ == "__main__" :
    app.run(debug=True ,port= 9000)