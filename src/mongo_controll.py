from pymongo import MongoClient
from config import Config

client = MongoClient(Config.MONGO_URI)
print("Connected to MongoDB!")

db = client["tieuyen"]

Users = db["users"]

Users.insert_one({
    "username": 'admin',
})