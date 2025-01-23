from pymongo.mongo_client import MongoClient
from Networksecurity.exception.exception import NetworkSecurityException
from Networksecurity.logging.logger import logging
import pandas as pd 
import numpy as np 
import pymongo
import sys
import json
import os

import certifi
ca = certifi.where()


from dotenv import load_dotenv
load_dotenv()

# Get the MongoDB URI 
uri = os.getenv("MONGO_URI")

class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def csv_to_json_convertor(self, file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)
            records = list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def insert_data_mongodb(self, records, database, collection):
        try:
            self.database = database
            self.collection = collection
            self.records = records

            self.mongo_client = pymongo.MongoClient(uri, tlsCAFile=certifi.where())
            self.database = self.mongo_client[self.database]
            
            self.collection = self.database[self.collection]
            self.collection.insert_many(self.records)
            return len(self.records)
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
if __name__ == '__main__':
    FILE_PATH = "Network_Data/phisingData.csv"
    DATABASE = "ML_PROJECT"
    COLLECTION = "user"
    networkobj = NetworkDataExtract()
    records = networkobj.csv_to_json_convertor(file_path=FILE_PATH)
    print(records)
    no_of_records = networkobj.insert_data_mongodb(records, DATABASE, COLLECTION)
    print(no_of_records)



    # client = MongoClient(uri)

# try:
#     client.admin.command('ping')
#     print("connected to mongo DB")
    
# except Exception as e:
#     print(e)    

