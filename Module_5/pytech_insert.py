#Milo Blake
#06/20/2021
#Module 5.3

#import statements
from pymongo import MongoClient

# MongoDB connection string 
url = "mongodb+srv://admin:admin@cluster0.lpnff.mongodb.net/pytech?retryWrites=true&w=majority"

# connect to the MongoDB cluster 
client = MongoClient(url)

# connect pytech database
db = client.pytech

""" three student documents"""
# Jane Doe 
jane = {
    "student_id": "1007",
    "first_name": "Jane",
    "last_name": "Doe",
    "enrollments": [
        {
            "term": "Summer",
            "gpa": "4.0",
            "start_date": "June 20, 2021",
            "end_date": "September 16, 2021",
            "courses": [
                {
                    "course_id": "CSD310",
                    "description": "Database Development and Use",
                    "instructor": "Professor Plato",
                    "grade": "A+"
                },
                {
                    "course_id": "CSD320",
                    "description": "Programming with Java",
                    "instructor": "Professor Plato",
                    "grade": "A+"
                }
            ]
        }
    ]

}

# John Wick 
john = {
    "student_id": "1008",
    "first_name": "John",
    "last_name": "Wick",
    "enrollments": [
        {
            "term": "Summer",
            "gpa": "4.0",
            "start_date": "June 20, 2021",
            "end_date": "September 16, 2021",
            "courses": [
                {
                    "course_id": "CSD310",
                    "description": "Database Development and Use",
                    "instructor": "Professor Plato",
                    "grade": "A+"
                },
                {
                    "course_id": "CSD320",
                    "description": "Programming with Java",
                    "instructor": "Professor Plato",
                    "grade": "A+"
                }
            ]
        }
    ]
}

# Allen Wrench
allen = {
    "student_id": "1009",
    "first_name": "allen",
    "last_name": "wrench",
    "enrollments": [
        {
            "term": "Summer",
            "gpa": "4.0",
            "start_date": "June 20, 2021",
            "end_date": "September 16, 2021",
            "courses": [
                {
                    "course_id": "CSD310",
                    "description": "Database Development and Use",
                    "instructor": "Professor Plato",
                    "grade": "A+"
                },
                {
                    "course_id": "CSD 320",
                    "description": "Programming with Java",
                    "instructor": "Professor Plato",
                    "grade": "A+"
                }
            ]
        }
    ]
}

# get the students collection 
students = db.students

# insert statements with output 
print("\n  -- INSERT STATEMENTS --")
jane_student_id = students.insert_one(jane).inserted_id
print("  Inserted student record Jane Doe into the students collection with document_id " + str(jane_student_id))

john_student_id = students.insert_one(john).inserted_id
print("  Inserted student record John Wick into the students collection with document_id " + str(john_student_id))

allen_student_id = students.insert_one(allen).inserted_id
print("  Inserted student record Allen Wrench into the students collection with document_id " + str(allen_student_id))

input("\n\n  End of program, press any key to exit... ")