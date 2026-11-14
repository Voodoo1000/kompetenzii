# Клонирование проекта
git clone https://github.com/Voodoo1000/kompetenzii.git

# Переход в проект
cd kompetenzii

# Запуск PostgreSQL
sudo service postgresql start

# Создание виртуального окружения
python3 -m venv venv

# Активация виртуального окружения
source venv/bin/activate

# Установка зависимостей
pip install -r requirements.txt


Затем создать .env в корне проекта:
DB_HOST=localhost
DB_PORT=5432
DB_NAME=octagon_db
DB_USER=octagon
DB_PASSWORD=12345


Инициализация базы:
python -m app.init_db


Запуск API:
uvicorn app.main:app --reload


Адреса приложения:
- Swagger: http://127.0.0.1:8000/docs
- Проверка состояния: http://127.0.0.1:8000/health