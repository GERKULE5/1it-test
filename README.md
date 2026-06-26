# 1it-test

## Инструкция по запуску

### 1. Установка

```bash
git clone https://github.com/GERKULE5/1it-test.git
cd 1it-test
```

### 2. Установка зависимостей

**Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

**Linux/macOS:**
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 3. Создание базы данных

```bash
python manage.py migrate
```

### 4. Создание пользователя для админки

```bash
python manage.py createsuperuser
```

### 5. Запуск сервера

```bash
python manage.py runserver
```

- Сервер доступен по адресу `http://127.0.0.1:8000/`
- Админка доступна по адресу `http://127.0.0.1:8000/admin`
