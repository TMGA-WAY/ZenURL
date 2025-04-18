import os

from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

class MongoDBConnection:
    def __init__(self):
        self.db_name = os.getenv("MONGO_DB_NAME", "None")
        self.host = os.getenv("MONGO_DB_HOST", "localhost")
        self.port = int(os.getenv("MONGO_DB_PORT", 27017))
        self.user = os.getenv("MONGO_DB_USER", "mongo")
        self.password = os.getenv("MONGO_DB_PASSWORD", "nopassword")


    def __str__(self):
        return f"MongoDBConnection(db_name={self.db_name}, host={self.host}, port={self.port})"

    def connect(self):
        try:
            client = MongoClient(
                host=self.host,
                port=self.port,
                username=self.user,
                password=self.password,
            )
            db = client[self.db_name]
            return db
        except Exception as e:
            print(f"Error connecting to MongoDB: {e}")
            raise e

    def create_collection(self, collection_name):
        db = self.connect()
        db.create_collection(collection_name)
        return db[collection_name]

    def drop_collection(self, collection_name):
        db = self.connect()
        db.drop_collection(collection_name)

    def get_collection(self, collection_name):
        db = self.connect()
        collection = db[collection_name]
        return collection

    def insert_document(self, collection_name, document):
        collection = self.get_collection(collection_name)
        result = collection.insert_one(document)
        return result.inserted_id

    def update_document(self, collection_name, query, update):
        collection = self.get_collection(collection_name)
        result = collection.update_one(query, update)
        return result.modified_count

    def get_collection_by_condition(self, collection_name, query):
        collection = self.get_collection(collection_name)
        document = collection.find(query)
        return document
