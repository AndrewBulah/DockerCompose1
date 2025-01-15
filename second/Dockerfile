# Этап 1: Сборка
FROM python:3.10-slim AS builder

# Устанавливаем зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем код приложения
COPY app.py .

# Этап 2: Запуск
FROM python:3.10-slim

# Копируем зависимости из этапа сборки
COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages

# Копируем код приложения
COPY app.py .

# Открываем порт, на котором будет слушать приложение
EXPOSE 8000

# Команда запуска приложения
CMD ["python", "app.py"]
