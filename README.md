# LinkLet — сокращатель ссылок

LinkLet — это веб-приложение для сокращения URL-адресов с аналитикой переходов.

## Возможности

- Сокращение длинных URL до коротких кодов (5 символов)
- Проверка дубликатов — одинаковые ссылки получают один код
- Подсчёт количества переходов
- Дата последнего перехода
- Адаптивный дизайн

## Технологии

- Django 4.2.30
- PostgreSQL 16
- Bootstrap 5.3.0
- pytest 8.3.3
- Docker / Docker Compose

## Запуск с Docker (рекомендуемый способ)

Самый быстрый способ запустить проект — использовать Docker.
```bash
docker-compose up --build
```
### Применить миграции (если запускаете впервые)
```bash
docker-compose exec web python manage.py migrate
```
### Создать суперпользователя
```bash
docker-compose exec web python manage.py createsuperuser
```
### Теперь проект доступен:

Сайт: http://localhost:8000/main/

Админка: http://localhost:8000/admin/

### Остановить контейнеры (после просмотра проекта)
```bash
docker-compose down
```

## Установка и запуск (без Docker)

### 1. Клонировать репозиторий

```bash
git clone https://github.com/ваш-логин/LinkLet.git
cd LinkLet
```
### 2. Создать виртуальное окружение

```bash
python -m venv venv
venv\Scripts\activate     # Windows
# source venv/bin/activate  # Linux/Mac
```
### 3. Установить зависимости
```bash
pip install -r requirements.txt
```
### 4. Настроить базу данных PostgreSQL
Создайте базу данных:

sql:
```
CREATE DATABASE linklet;
```
Убедитесь, что настройки подключения в файле LinkLet/settings.py соответствуют вашим параметрам.
### 5. Применить миграции
```bash
python manage.py migrate
```
### 6. Создать суперпользователя для админки (опционально)
```bash
python manage.py createsuperuser
```
Введите логин и пароль для входа в админ-панель: http://127.0.0.1:8000/admin/

### 7. Запустить сервер
```bash
python manage.py runserver
```
Откройте в браузере: http://127.0.0.1:8000/main/

## Переменные окружения
Для работы проекта необходимо создать файл .env в корневой папке.
В нём должны быть указаны следующие переменные (пример можно взять из .env.example):

```
SECRET_KEY=ваш-секретный-ключ
DB_NAME=linklet
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=localhost
DB_PORT=5432
```
Если вы используете Docker, переменные уже заданы в docker-compose.yml, поэтому .env нужен только для локального запуска без Docker.

## Запуск тестов
```bash
pytest main/tests/ -v
```

## Админ-панель
После создания суперпользователя вы можете управлять ссылками через админку:

http://127.0.0.1:8000/admin/

В админке доступно:

Просмотр всех созданных ссылок

Поиск по короткому коду или оригинальному URL

Просмотр количества переходов

Деактивация ссылок

Удаление ссылок

## Структура проекта
```
LinkLet/
├── main/                # Основное приложение
│   ├── migrations/      # Миграции базы данных
│   ├── __init__.py
│   ├── admin.py         # Настройка админки
│   ├── apps.py          # Конфигурация приложения
│   ├── forms.py         # Форма для URL
│   ├── logger.py        # Настройка логирования
│   ├── models.py        # Модель Link
│   ├── tests/           # Тесты
│   │   ├── __init__.py
│   │   ├── test_views.py        # Модульные тесты
│   │   ├── test_integration.py  # Интеграционные тесты
│   ├── urls.py          # Маршруты приложения
│   ├── views.py         # Логика приложения
│   ├── static/          # CSS, изображения
│   └── templates/       # Шаблоны
├── linkLet/             # Настройки проекта
│   ├── __init__.py
│   ├── settings.py      # Настройки проекта
│   ├── urls.py          # Главные маршруты
│   └── wsgi.py          # Для деплоя
├── Dockerfile           # Docker-образ
├── docker-compose.yml   # Docker Compose
├── .dockerignore        # Исключения для Docker
├── requirements.txt     # Зависимости
├── README.md
├── .gitignore
└── manage.py
```
## Автор
Магасумова Альвина — [GitHub](https://github.com/Alvina-Magasumova)