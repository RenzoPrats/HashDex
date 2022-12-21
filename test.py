#Software Engineering Internship Challenge
#Candidate: Renzo Prats Silva Souza

#Importing libraries that will be used for develop the API
import unittest
import requests

#Creating the Test
class ApiTest(unittest.TestCase):
    API_URL = "http://localhost:5000"
    STUDENTS_URL = "{}/students".format(API_URL)
    STUDENT_URL = "{}/student".format(API_URL)
    
    #Test 1 select all students
    def test_1_select_students(self):
        r = requests.get(ApiTest.STUDENTS_URL)
        self.assertEqual(r.status_code, 200)
    
    #Test 2 create a student
    def test_2_create_student(self):
        new_student_obj = {
            "id" : 1,
            "name" : "Vini Jr",
            "email" : "vnjunior@hotmail.com",
            "registration" : "11921EEL002"
        }
        r = requests.post(ApiTest.STUDENT_URL, json=new_student_obj)
        self.assertEqual(r.status_code, 201)
    
    #Test 3 checks if exists the student created in test 2 and if it's right the values of its fields
    def test_3_select_student(self):
        id = 1
        student_obj_return = {
            "student": {
                "id": 1,
                "name": "Vini Jr",
                "email": "vnjunior@hotmail.com",
                "registration": "11921EEL002"
            },
            "message": "OK"
        }
        r = requests.get("{}/{}".format(ApiTest.STUDENT_URL,id))
        self.assertEqual(r.status_code,200)
        self.assertDictEqual(r.json(), student_obj_return)
    
    #Test 4 create a student
    def test_4_create_student(self):
        new_student_obj = {
            "id" : 2,
            "name" : "Casemiro Silva",
            "email" : "casemirosilva@hotmail.com",
            "registration" : "11921EEL003"
        }
        r = requests.post(ApiTest.STUDENT_URL, json=new_student_obj)
        self.assertEqual(r.status_code, 201)
    
    
    #Test 5 checks if exists the student created in test 4 and if it's right the values of its fields
    def test_5_select_student(self):
        id = 2
        student_obj_return = {
            "student": {
                "id": 2,
                "name": "Casemiro Silva",
                "email": "casemirosilva@hotmail.com",
                "registration": "11921EEL003"
            },
            "message": "OK"
        }
        r = requests.get("{}/{}".format(ApiTest.STUDENT_URL,id))
        self.assertEqual(r.status_code,200)
        self.assertDictEqual(r.json(), student_obj_return)
    
    #Test 6 updates the student created on test 2 and verify if it was updated correctly
    def test_6_update_student(self):
        id = 1
        new_student_obj = {
            "name" : "Ronaldo Fenomeno",
            "email" : "rf@hotmail.com"
        }
        
        new_student_obj_return = {
            "student": {
                "id": 1,
                "name": "Ronaldo Fenomeno",
                "email": "rf@hotmail.com",
                "registration": "11921EEL002"
            },
            "message": "Successfully updated"
        }
        r = requests.put("{}/{}".format(ApiTest.STUDENT_URL,id), json=new_student_obj)
        self.assertEqual(r.status_code,200)
        self.assertDictEqual(r.json(), new_student_obj_return)
    
    #Test 7 deletes the student created on test 4
    def test_7_delete_student(self):
        id = 2
        r = requests.delete("{}/{}".format(ApiTest.STUDENT_URL,id))
        self.assertEqual(r.status_code, 200)
        

#run test.py
if __name__ == '__main__':
    unittest.main()