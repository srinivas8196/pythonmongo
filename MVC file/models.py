from pymongo import MongoClient
from bson import ObjectId

client = MongoClient('mongodb://localhost:27017/')
db = client['your_db_name']


class Blog:
    @staticmethod
    def to_json(post):
        return {
            "id": str(post["_id"]),
            "title": post["title"],
            "content": post["content"]
        }
