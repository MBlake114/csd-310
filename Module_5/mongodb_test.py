#Milo Blake
#06/20/2021

# import statments
from pymongo import MongoClient

# MongoDB connection string 
url = "mongodb+srv://admin:admin@cluster0.lpnff.mongodb.net/pytech?retryWrites=true&w=majority"

# Connect to the MongoDB cluster 
client = MongoClient(url)

# Connect pytech database
db = client.pytech

# Show the connected collections 
print("\n Pytech COllection List")
print(db.list_collection_names())

# Show an exit message
input("\n\n  End of program, press any key to exit. ")