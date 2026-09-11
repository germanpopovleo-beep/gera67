FROM python:3.10-slim

# Создаем системную группу и пользователя appuser
RUN addgroup --system appgroup && adduser --system --ingroup appgroup appuser

WORKDIR /app

# Копируем и устанавливаем зависимости от root
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем остальной исходный код (без файлов из .dockerignore)
COPY . .

# Меняем владельца файлов папки /app на appuser
RUN chown -R appuser:appgroup /app

# Переключаемся на non-root пользователя перед запуском приложения
USER appuser

EXPOSE 5000

CMD ["python", "app.py"]