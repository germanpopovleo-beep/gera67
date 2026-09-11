import os
from flask import Flask, jsonify

app = Flask(__name__)

# Чтение переменных окружения
APP_ENV = os.getenv("APP_ENV", "development")
SECRET_KEY = os.getenv("SECRET_KEY", "default_secret")
DATABASE_URL = os.getenv("DATABASE_URL", "not_set")
DEBUG = os.getenv("DEBUG", "True").lower() == "true"

@app.route("/")
def index():
    return jsonify({
        "message": "App is running",
        "app_env": APP_ENV,
        "database_url": DATABASE_URL,
        "debug": DEBUG
    })

@app.route("/config")
def config():
    # Демонстрация чтения секретов и окружения
    return f"Environment: {APP_ENV}, Secret key length: {len(SECRET_KEY)}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=DEBUG)