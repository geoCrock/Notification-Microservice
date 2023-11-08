FROM python:3.11

WORKDIR /app

RUN pip install -r requirements.txt

COPY . .

CMD["python", "server.py"]