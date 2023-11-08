from flask import jsonify
from app.mongo_connector import MongoDB
from app.email_sender import EmailSender
from app.config import Config

mongo = MongoDB()
email_sender = EmailSender()


def create_notification(request):
    data = request.get_json()
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    user_id = data.get("user_id")
    key = data.get("key")
    target_id = data.get("target_id")
    data_content = data.get("data")

    # Limit of maximum amount of notifications
    if mongo.db.notifications.count_documents({"user_id": user_id}) >= 10:
        return jsonify({'success': False, "reason": 'Limit of notifications'})

    if key != 'registration':
        mongo.create_notification(user_id, {
            "key": key,
            "target_id": target_id,
            "data": data_content
        })

    # if send an email is required
    if key == "new_login" or key == "registration":
        email_subject = "New Notification"
        email_body = f"You have a new notification: {data_content}"
        email_to = Config.EMAIL

        email_sender.send_email(email_to, email_subject, email_body)

    return jsonify({"success": True}), 201


def list_notifications(request):
    user_id = str(request.args.get("user_id"))
    skip = int(request.args.get("skip", 0))
    limit = int(request.args.get("limit", 10))

    try:
        notifications = mongo.get_notifications(user_id, skip, limit)

        total_elements = mongo.get_total_notifications_count(user_id)
        new_elements = mongo.get_unread_notifications_count(user_id)

        response_data = {
            "elements": total_elements,
            "new": new_elements,
            "request": {
                "user_id": user_id,
                "skip": skip,
                "limit": limit
            },
            "list": notifications
        }

        return jsonify({"success": True, "data": str(response_data)}), 200

    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


def mark_as_read(request):
    user_id = request.args.get("user_id")
    notification_id = request.args.get("notification_id")

    success = mongo.mark_as_read(user_id, notification_id)

    return jsonify({"success": success}), 200
