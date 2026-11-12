# Базовый образ
FROM python:3.11-slim

# Настройки Python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Рабочая папка внутри контейнера
WORKDIR /app

# Устанавливаем системные зависимости для psycopg2 (PostgreSQL)
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Копируем зависимости и устанавливаем их
COPY requirements.txt /app/
RUN pip install --default-timeout=1000 --no-cache-dir -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com

# Копируем весь код проекта
COPY . /app/

# Открываем порт
EXPOSE 8000

# Запускаем сервер
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
