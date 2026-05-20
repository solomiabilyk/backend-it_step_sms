#!/bin/sh

# Якщо якась команда завершиться помилкою, скрипт одразу зупиниться (корисно для дебагу)
set -e

echo "--> Очікування запуску бази даних PostgreSQL..."
# Перевіряємо доступність бази за допомогою python-коду (щоб не встановлювати netcat)
python << END
import sys
import socket
import time

port = int("${DB_PORT:-5432}")
host = "${DB_HOST:-db}"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
while True:
    try:
        s.connect((host, port))
        s.close()
        break
    except socket.error:
        print("База даних ще недоступна, чекаємо 1 секунду...")
        time.sleep(1)
END

echo "--> База даних готова!"

echo "--> Виконання міграцій..."
python manage.py migrate --noinput

echo "--> Збір статичних файлів (якщо потрібно для production)..."
# python manage.py collectstatic --noinput

# exec "$@" означає: виконати команду, яку передали в контейнер як CMD
# У нашому випадку це буде запуск Gunicorn або runserver
echo "--> Запуск фінальної команди розгортання..."
exec "$@"