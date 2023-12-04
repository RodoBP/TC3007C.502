import pymongo
import json
import csv

# Establish a connection to the MongoDB server
client = pymongo.MongoClient("mongodb+srv://Rodo:rodo1997@rodo.okvlagw.mongodb.net/?retryWrites=true&w=majority")

# Access the desired database
db = client["your_db_name"]

# Access the desired collection
collection = db["your_collection_name"]

# Read data from your dataset csv
with open('albumlist.csv') as f:
    data = [{k: v for k, v in row.items()}
        for row in csv.DictReader(f, skipinitialspace=True)]

# Insert data into the collection
collection.insert_many(data)