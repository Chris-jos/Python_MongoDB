from db_connection import db
from typing import List, Dict

def insert_single_document(collection: str, document: dict):
    db[collection].insert_one(document)

def insert_multiple_document(collection: str, l_document: List[Dict]):
    db[collection].insert_many(l_document)

def find_one(collection: str, filter: Dict = None):
    return db[collection].find_one(filter)

def find_all(collection: str, filter: Dict = None, columns: Dict = None):
    filter = filter or {}
    return db[collection].find(filter, columns)

def count_of_docs(collection: str, filter: Dict = None):
    filter = filter or {}
    return db[collection].count_documents(filter)