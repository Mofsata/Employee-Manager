# Employee-Manager-API

A simple REST API using Flask.
This API function as system where you can manage the information of your employees.

The Information is stored on a SQLite database table, and the parameters of each row are [Id, Name, Job Title, Age, Salary].

And the operations you can do with this API are defined in these HTTP requests:

## HTTP Requests

### GET All Employees

<https://localhost:9000/>

Returns all the Employees stored on the database.

### GET Employee by ID

<https://localhost:9000/{id}>

The {id} integer represents the id of the Employee in the database.

### POST An Employee

<https://localhost:9000/>

The body of the request should have a JSON object like this:

```JSON
{
    "Name": "fullname",
    "JobTitle": "job title",
    "Age": 22,
    "Salary": 3000 
}
```

### PUT An Employee

<https://localhost:9000/{id}>

The {id} integer represents the id of the Employee in the database.

The data parameters are received via the body of the request as a form-data where the key section should have the parameter's name and the new value should be in the value section.

### DELETE Employee by ID

<https://localhost:9000/{id}>

The {id} integer represents the id of the Employee in the database.
