# Використовуємо офіційний легкий образ Python
FROM python:3.13-slim

# Встановлюємо змінні оточення для Python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Створюємо робочу папку всередині контейнера
WORKDIR /app

# Копіюємо файл із залежностями та встановлюємо їх
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Копіюємо весь код проекту
COPY . /app/

# Відкриваємо порт
EXPOSE 8000

# Запускаємо міграції, збираємо статику і стартуємо Gunicorn
CMD python manage.py migrate && \
    python manage.py collectstatic --noinput && \
    gunicorn project.wsgi:application --bind 0.0.0.0:${PORT:-8000}