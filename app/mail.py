import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Замените следующие переменные своими данными
sender_email = "georgiy.shvelev.era@yandex.ru"
sender_password = "fdsafadsfa445"
receiver_email = "georgiy.shvelev.era@yandex.ru"
subject = "Тема вашего письма"
body = "Текст вашего письма"

# Создаем объект MIMEMultipart
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

# Добавляем текст письма в тело сообщения
message.attach(MIMEText(body, "plain"))

# Создаем объект сервера SMTP
server = smtplib.SMTP("smtp.yandex.ru", 587)

# Устанавливаем соединение с сервером
server.starttls()

# Логинимся в учетной записи отправителя
server.login(sender_email, sender_password)

# Отправляем письмо
server.send_message(message)

# Закрываем соединение с сервером
server.quit()
