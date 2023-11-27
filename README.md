# Microservice Notification System

Данное приложение представляет из себя RESTful API сервер для управления уведомлениями пользователей. Сервис позволяет создавать, получать список и отмечать уведомления как прочитанные. А так же посылать email с любым текстом врутри.
  
Стэк: Flask, MongoDB.

## Использование
#### Пример уведомления в документе пользователя
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

### [POST] /create создает новое уведомление.

#### Тело запроса:

- user_id - строка на 24 символа (является ObjectID документа пользователя которому отправляется уведомление)
- target_id - строка на 24 символа (является ObjectID документа сущности, к которой относится уведомление) (Может отсутствовать)
- key - ключ уведомления enum
    - registration (Только отправит пользователю Email)
    - new_message (только создаст запись в документе пользователя)
    - new_post (только создаст запись в документе пользователя)
    - new_login (Создаст запись в документе пользователя и отправит email)
- data - произвольный объект из пар ключ/значение (Может отсутствовать)

#### Пример тела запроса:

```json
{
    "user_id": "638f394d4b7243fc0399ea67",
    "key": "registration",
}
```

#### Пример ответа

HTTP 201 Created

```json
{
    "success": true,
}
```

### [GET] /list производит листинг уведомлений пользователя.

#### query params
- user_id [string] - идентификатор пользователя
- skip [int] - кол-во уведомлений, которые следует пропустить
- limit [int] - кол-во уведомлений которые следует вернуть

#### Пример ответа

HTTP 200 Ok

```json
{
    "success": true,
    "data": {
        "elements": 23, // всего уведомлений
        "new": 12, // Кол-во непрочитанных уведомлений
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

#### [POST] /read создает отметку о прочтении уведомления.

#### query params
- user_id [string] - идентификатор пользователя
- notification_id [string] - Идентификатор уведомления

#### Пример ответа

HTTP 200 Ok

```json
{
    "success": true,
}
```


## Основные компоненты

- `server.py`: Основной файл, содержащий код для запуска RESTful API сервера.
- `mongo_connector.py`: Модуль для работы с базой данных MongoDB.
- `email_sender.py`: Модуль для отправки уведомлений по электронной почте.
- `notification_handler.py`: Обработчики запросов API.

## Переменные окружения

Для конфигурации сервиса используются следующие переменные окружения:

- `PORT`: Порт, на котором будет работать приложение.
- `DB_URI`: Строка для подключения к MongoDB.
- `SMTP_HOST`: Хост SMTP-сервера.
- `SMTP_PORT`: Порт SMTP-сервера.
- `SMTP_LOGIN`: Логин пользователя SMTP.
- `SMTP_PASSWORD`: Пароль пользователя SMTP.
- `SMTP_EMAIL`: Email, с которого будут отправляться уведомления.
- `SMTP_NAME`: Имя отображаемое у получателя письма.

## Запуск

Перед запуском не забудьте создать и активировать виртуальное окружение

1. Склонируйте репозиторий:

    ```bash
    git clone https://github.com/geoCrock/AsyncMessagesQueue.git
    ```

2. Перейдите в директорию проекта:

    ```bash
    cd AsyncMessagesQueue
    ```

3. Создайте файл `.env` в корне проекта и укажите необходимые переменные окружения.


## Запуск через Docker

1. Установите зависимости: `pip install -r requirements.txt`
2. Запустите контейнер Docker: `docker build -t notification-service . && docker run -p 5000:5000 --env-file .env notification-service`
