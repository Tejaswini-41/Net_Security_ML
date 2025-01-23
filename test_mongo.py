from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

uri = os.getenv("MONGO_URI") 

client = MongoClient(uri)

try:
    client.admin.command('ping')
    print("connected to mongo DB")
    
except Exception as e:
    print(e)    