#Milo Blake
#06/26/2021
#Module 6.3

#import statements
from pymongo import MongoClient

# MongoDB connection string 
url = "mongodb+srv://admin:admin@cluster0.lpnff.mongodb.net/pytech?retryWrites=true&w=majority"

# connect to the MongoDB cluster 
client = MongoClient(url)

# connect pytech database
db = client.pytech

# get the students collection 
students = db.students

# find all students in the collection 
student_list = students.find({})

# display message 
print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

# loop over the collection and output the results 
for doc in student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

# Mac Intosh doc 
mac = {
    "student_id": "1010",
    "first_name": "Mac",
    "last_name": "Intosh",
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
#display insert statement
print("\n  -- INSERT STATEMENTS --")
mac_student_id = students.insert_one(mac).inserted_id
print("  Inserted student record Mac Intosh into the students collection with document_id " + str(mac_student_id))

#Find the student_id 1010 doc
mac = students.find_one({"student_id": "1010"})

#output the document to terminal window
print("\n  Student ID: " + mac["student_id"] + "\n  First Name: " + mac["first_name"] + "\n  Last Name: " + mac["last_name"] + "\n")

# find all students in the collection 
student_list = students.find({})

# display message 
print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

# loop over the collection and output the results 
for doc in student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

#exit message
input("\n\n  End of program, press an key to continue...")