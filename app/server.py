from flask import Flask, request, jsonify
from app.notification_handler import create_notification, list_notifications, mark_as_read
from app.config import Config

app = Flask(__name__)


@app.route("/create", methods=["POST"])
def create_notification_route():
    if request.headers["Content-Type"] == "application/json":
        return create_notification(request)
    else:
        return jsonify({"error": "Unsupported Media Type"}), 415


@app.route("/list", methods=["GET"])
def list_notifications_route():
    return list_notifications(request)


@app.route("/read", methods=["POST"])
def mark_as_read_route():
    return mark_as_read(request)


if __name__ == "__main__":
    app.run(port=Config.PORT)
