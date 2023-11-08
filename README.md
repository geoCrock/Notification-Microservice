# Microservice Notification System

Microservice Notification System представляет из себя RESTful API сервер для управления уведомлениями пользователей. Сервис позволяет создавать, получать список и отмечать уведомления как прочитанные.

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

## Запуск сервиса

1. Установите зависимости: `pip install -r requirements.txt`
2. Запустите контейнер Docker: `docker build -t notification-service . && docker run -p 5000:5000 --env-file .env notification-service`
