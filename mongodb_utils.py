from pymongo import MongoClient
from config import MONGO_URI, DB_NAME, COLLECTION_NAME

def get_db():
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    return db

def insert_traffic_record(record):
    db = get_db()
    db[COLLECTION_NAME].insert_one(record)

def get_latest_records(limit=10):
    db = get_db()
    return list(db[COLLECTION_NAME].find().sort("timestamp", -1).limit(limit))
