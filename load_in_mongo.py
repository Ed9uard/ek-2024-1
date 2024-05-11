from pymongo import MongoClient
from pymongo.server_api import ServerApi
import json

client = MongoClient(
    "mongodb+srv://ed9uard:MGuHLevfZhdvw3Ru@cluster0.wkfa92c.mongodb.net/",
    server_api=ServerApi('1')
)

db = client.hm3 
authors_collection = db.authors
quotes_collection = db.quotes

with open('quotes.json', 'r', encoding='utf-8') as quotes_file:
    quotes_data = json.load(quotes_file)

quotes_collection.insert_many(quotes_data)

with open('authors.json', 'r', encoding='utf-8') as authors_file:
    authors_data = json.load(authors_file)

authors_collection.insert_many(authors_data)
print("Дані імпортовано")

client.close()