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

# get the students collection 
students = db.students

# find all students in the collection 
student_list = students.find({})

# display message 
print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

# loop over the collection and output the results 
for doc in student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

# update student_id 1007
result = students.update_one({"student_id": 1007}, {"$set": {"last_name": "Johnson"}})

#Find the updated student doc
jane = students.find_one({"student_id": "1007"})

#display message
print("\n -- DISPLAYING STUDENT DOCUMENT 1007 --")

#output the updated document to terminal window
print("\n  Student ID: " + jane["student_id"] + "\n  First Name: " + jane["first_name"] + "\n  Last Name: " + jane["last_name"] + "\n")

#exit message
input("\n\n  End of program, press an key to continue...")
