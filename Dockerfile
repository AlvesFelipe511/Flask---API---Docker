FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN apt-get update && apt-get install -y netcat-openbsd

RUN chmod +x /app/wait-for-it.sh

RUN pip install --no-cache-dir -r requirements.txt

ENV FLASK_APP=app.py