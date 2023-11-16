# Microservice Notification System

Это моё выполнение тестировочное задание от компании ООО Эйс Плэйс

Данное приложение представляет из себя RESTful API сервер для управления уведомлениями пользователей. Сервис позволяет создавать, получать список и отмечать уведомления как прочитанные.
  
  Стэк: Flask, MongoDB.

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

## Мои решения и подходы

Для теста запросов я использовал Postman.

Я не совсем точно понял некоторые пункты в задаче, например:
1. Я не понял что значит "Имя отображаемое у получателя письма" и ее переменная "SMTP_NAME", поэтому эту переменную можно добавить в код в качестве переменной окружения, но она не используется.
2. Не было указания, что присылать в теле письма, которое должно прийти на email, поэтому я использовал для этого переменную "data" из метода /create.
3. Я не совсем понял как это всё должно работать в БД с документом пользователя и нужно ли вообще его создавать в БД, поэтому в БД есть только записи об уведомлениях и никаких таблиц "user".
В силу этого не понимания, сервис может отличаться от того, что было задумано изначально.
