#Software Engineering Internship Challenge
#Candidate: Renzo Prats Silva Souza

#Importing libraries that will be used for develop the API
from flask import Flask, Response, request
from flask_sqlalchemy import SQLAlchemy
import json
import os

#Configuring the flask aplication and database
app = Flask(__name__)
app.app_context().push()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:////{os.path.abspath("")}/students.db'


db = SQLAlchemy(app)



#Creating the object Student
class Student(db.Model):
    #field that represent the identifier(id)
    id = db.Column(db.Integer, primary_key=True)
    #field that represent the name of the student
    name = db.Column(db.String(200))
    #field that represent the email of the student
    email = db.Column(db.String(100), unique=True)
    #field that represent the registration of the student
    registration = db.Column(db.String(20), unique=True)
    
    #method that converts the fields of the object to json
    def to_json(self):
        return {"id": self.id, "name": self.name, "email": self.email, "registration": self.registration}


db.drop_all()
db.create_all()


#function that generate the response for the CRUD functions
def generate_response(status, content_name, content, message=False):
    body = {}
    body[content_name] = content
     
    if message:
        body["message"] = message
        
    return Response(json.dumps(body), status=status, mimetype="application/json")


#Routes

#route /students that return all students in the json format
@app.route("/students", methods=["GET"])
def select_students():
    try:
        #select all students objects
        students_objects = Student.query.all()
        #convert all students objects to json
        students_json = [student.to_json() for student in students_objects]
        
        #return a list of all student and a sucessfully message
        return generate_response(200, "students", students_json, "OK")
    
    #if try fails then returns empty and a error message
    except:
        return generate_response(400, "students", {}, "Error when filtering")


#route /student/<id> that return a student by passing its id 
@app.route("/student/<id>", methods=["GET"])
def select_student(id):
    #select student by its id
    student_object = Student.query.filter_by(id=id).first()
    
    #Try return the student filtered by its id
    try:
        student_json = student_object.to_json()
        #return the student filtred and a sucessfully message
        return generate_response(200, "student", student_json, "OK")
    
    #if try fails then returns empty and a error message
    except:
        return generate_response(400, "student", {}, "Error when filtering")
    


#route /student that creates a student by the method HTTP POST
@app.route("/student", methods=["POST"])
def create_student():
    body = request.get_json()
    
    #try creates a student by passing the parameters name, email and registration
    try:
        student = Student(name=body["name"], email=body["email"], registration=body["registration"])
        db.session.add(student)
        db.session.commit()
        #return the student created and a sucessfully message
        return generate_response(201, "student", student.to_json(), "Successfully created")
    
    #if try fails then returns empty and a error message
    except:
        return generate_response(400, "student", {}, "Error when registering")


#route /student/<id> that update a student by the method HTTP PUT
@app.route("/student/<id>", methods=["PUT"])
def update_student(id):
    #filter the student by id
    student_object = Student.query.filter_by(id=id).first()
    body = request.get_json()

    #try to update this student by the parameters that could be passed
    try:
        if('name' in body):
            student_object.name = body['name']
        if('email' in body):
            student_object.email = body['email']
        if('registration' in body):
            student_object.registration = body['registration']
        
        db.session.add(student_object)
        db.session.commit()
        #return the student updated and a sucessfully message
        return generate_response(200, "student", student_object.to_json(), "Successfully updated")
    
    #if try fails then returns empty and a error message
    except:
        return generate_response(400, "student", {}, "Error when updating")


#route /student/<id> that delete a student by the method HTTP DELETE
@app.route("/student/<id>", methods=["DELETE"])
def delete_student(id):
    #filter the student by id
    student_object = Student.query.filter_by(id=id).first()
    
    #try to delete this student
    try:
        db.session.delete(student_object)
        db.session.commit()
        #return the deleted student and a sucessfully message
        return generate_response(200, "student", student_object.to_json(), "Successfully deleted")
    
    #if try fails then returns empty and a error message
    except:
        return generate_response(400, "student", {}, "Error deleting")
        

#run the app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')