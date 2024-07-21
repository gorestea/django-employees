- Django
- DRF
- PostgreSQL
- uWSGI + Nginx
- Sentry
- Docker
- Docker Compose

## Настройка

1. **Клонируйте репозиторий:**

   ```sh
   git clone https://github.com/gorestea/django-employees.git
   ```

2. Настройте company/.env

3. Локальный запуск. Либо (если запускать через docker-compose) переходите к следующему шагу.

  ```sh
  pip install requirements.txt
  python manage.py makemigrations
  python manage.py migrate
  python manage.py test employees/tests
  python manage.py create_db
  python manage.py createsuperuser
  python manage.py runserver
  ```

4. Соберите и запустите Docker контейнеры:

  ```sh
  docker-compose build
  docker-compose up
  ```

Django приложение будет доступно по адресу http://localhost:8001.
Nginx - http://localhost:80

**Данные для админки: login - admin, pass - adminpass (из create_admin.py)**

