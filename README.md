# Microservice Notification System

This application is a RESTful API server for managing user notifications. The service allows you to create, receive a list and mark notifications as read. And also send an email with any text inside.
  
Stack: Flask, MongoDB.

## Usage
#### Example of a notification in a user document
```json
{
     "id": "some_notification_id",
     "timestamp": 1698138241,
     "is_new": false,
     "user_id": "638f394d4b7243fc0399ea67",
     "key": "new_message",
     "target_id": "0399ea67638f394d4b7243fc",
     "data": {
         "some_field": "some_value"
     },
},
```
## API Handlers:

### [POST] /create creates a new notification.

#### Request body:

- user_id - a 24-character string (is the ObjectID of the user document to which the notification is sent)
- target_id - a 24-character string (is the ObjectID of the document of the entity to which the notification relates) (May be absent)
- key - notification key enum
     - registration (Only sends email to user)
     - new_message (will only create an entry in the user’s document)
     - new_post (will only create a post in the user’s document)
     - new_login (Creates an entry in the user’s document and sends an email)
- data - an arbitrary object of key/value pairs (May be absent)

#### Example request body:

```json
{
     "user_id": "638f394d4b7243fc0399ea67",
     "key": "registration",
}
```

#### Sample answer

HTTP 201 Created

```json
{
     "success": true,
}
```

### [GET] /list lists user notifications.

#### query params
- user_id [string] - user identifier
- skip [int] - number of notifications that should be skipped
- limit [int] - number of notifications that should be returned

#### Sample answer

HTTP 200 Ok

```json
{
     "success": true,
     "data": {
         "elements": 23, // total notifications
         "new": 12, // Number of unread notifications
         "request": {
             "user_id": "638f394d4b7243fc0399ea67",
             "skip": 0,
             "limit": 10,
         }
         "list": [
             {
                 "id": "some_notification_id",
                 "timestamp": 1698138241,
                 "is_new": false,
                 "user_id": "638f394d4b7243fc0399ea67",
                 "key": "new_message",
                 "target_id": "0399ea67638f394d4b7243fc",
                 "data": {
                     "some_field": "some_value"
                 },
             },
             ...
         ]
     }
}
```

#### [POST] /read creates a read mark for the notification.

#### query params
- user_id [string] - user identifier
- notification_id [string] - Notification ID

#### Sample answer

HTTP 200 Ok

```json
{
     "success": true,
}
```


## Main components

- `server.py`: The main file containing the code to run the RESTful server API.
- `mongo_connector.py`: Module for working with the MongoDB database.
- `email_sender.py`: Module for sending notifications by email.
- `notification_handler.py`: API request handlers.

## Environment variables

The following environment variables are used to configure the service:

- `PORT`: Port on which the application will run.
- `DB_URI`: String to connect to MongoDB.
- `SMTP_HOST`: Host of the SMTP server.
- `SMTP_PORT`: SMTP server port.
- `SMTP_LOGIN`: SMTP user login.
- `SMTP_PASSWORD`: SMTP user password.
- `SMTP_EMAIL`: Email from which notifications will be sent.
- `SMTP_NAME`: The name displayed for the recipient of the message.

## Launch

Before starting, do not forget to create and activate a virtual environment

1. Clone the repository:

     ```bash
     git clone https://github.com/geoCrock/Notification-Microservice.git
     ```

2. Go to the project directory:

     ```bash
     cd Notification-Microservice
     ```

3. Create a `.env` file in the project root and specify the necessary environment variables:
    Specify your parameters
   
5. Run main.py in the app folder:
    ```bash
     cd app
     ```

    ```bash
     server.py
     ```
   

## Running via Docker

Before starting, do not forget to create and activate a virtual environment

1. Clone the repository:

     ```bash
     git clone https://github.com/geoCrock/AsyncMessagesQueue.git
     ```

2. Go to the project directory:

     ```bash
     cd AsyncMessagesQueue
     ```

3. Create a `.env` file in the project root and specify the necessary environment variables.


Make sure the following components are installed on your system:

-Docker
- Docker Compose

1. Clone the repository:

     ```bash
     git clone https://github.com/geoCrock/Notification-Microservice.git
     ```

2. Go to the project directory:

     ```bash
     cd Notification-Microservice
     ```

3. Create a `.env` file in the project root and specify the necessary environment variables:
    Specify your parameters

5. Build and run Docker containers:

     ```bash
     docker-compose up --build
     ```
