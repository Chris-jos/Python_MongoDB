from dotenv import load_dotenv, find_dotenv
import os
from pymongo import MongoClient
load_dotenv(find_dotenv())

db_password = os.environ.get("MONGODB_PWD")
user = os.environ.get("MONGODB_USR")

connection_string = f"mongodb+srv://{user}:{db_password}@clustercj.cw5cdoi.mongodb.net/?retryWrites=true&w=majority&appName=clusterCJ"
client = MongoClient(connection_string)

dbs = client.list_database_names() # list db names
db = client.production
