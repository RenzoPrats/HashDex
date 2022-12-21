# Hashdex Software Engineering Internship Challenge
This program is a CRUD API for working with student data. It's possible to do CRUD operations by running the aplication server and send requests by some software like Postman and Insomnia. Following will be the URL, the method and which operation is performed:
* GET http://localhost:5000/students lists all the students in database
* GET http://localhost:5000/student/id lists the student by id in database
* POST http://localhost:5000/student creates a new student by passing the values by JSON
* PUT http://localhost:5000/student/id updates the student with this id
* DELETE http://localhost:5000/student/id deletes the student with this id

the structure of the JSON student is:
{
  "id" : value,
  "name" : "value",
  "email" : "value",
  "registration", "value"
}

## Compilation:
On linux after install docker, you can compile and run in your project folder using:
```shell
sudo docker build -t api .
sudo docker run -p 5000:5000 api
```
Then the URLs will be available for access via Postman or Insomnia and similar softwares. It's also possible run the unit tests created for test the API by opening another shell and run in your project folder:
```shell
python test.py
```
