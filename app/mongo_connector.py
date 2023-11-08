from pymongo import MongoClient
from bson import ObjectId
from app.config import Config
from datetime import datetime
from flask import jsonify


class MongoDB:
    def __init__(self):
        self.client = MongoClient(Config.DB_URI)
        self.db = self.client.get_default_database()

    def create_notification(self, user_id, notification):
        notifications_collection = self.db.notifications

        # Add notification to the collection
        notification["user_id"] = user_id
        notification["timestamp"] = int(datetime.now().timestamp())
        notification["is_new"] = True

        result = notifications_collection.insert_one(notification)

        return str(result.inserted_id)

    def get_notifications(self, user_id, skip=0, limit=10):
        notifications_collection = self.db.notifications

        # Get notification form the collection
        cursor = notifications_collection.find({"user_id": user_id}).sort("timestamp", -1).skip(skip).limit(limit)
        notifications = list(cursor)

        return notifications

    def mark_as_read(self, user_id, notification_id):
        notifications_collection = self.db.notifications

        result = notifications_collection.update_one(
            {"_id": ObjectId(notification_id), "user_id": user_id},
            {"$set": {"is_new": False}}
        )

        return result.modified_count > 0

    def get_total_notifications_count(self, user_id):
        notifications_collection = self.db.notifications
        return notifications_collection.count_documents({"user_id": user_id})

    def get_unread_notifications_count(self, user_id):
        notifications_collection = self.db.notifications
        return notifications_collection.count_documents({"user_id": user_id, "is_new": True})
