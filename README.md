- Docker
- Docker Compose

## Настройка

1. **Клонируйте репозиторий:**

   ```sh
   git clone https://github.com/gorestea/django-employees.git
   ```

2. Установите зависимости для запуска локально. Либо переходите к следующему шагу.

  ```sh
  pip install requirements.txt
  ```

3. Настройте company/.env

4. Соберите и запустите Docker контейнеры:

  ```sh
  docker-compose build
  docker-compose up
  ```

Django приложение будет доступно по адресу http://localhost:8001.
Nginx - http://localhost:80

**Данные для админки: login - admin, pass - adminpass (из create_admin.py)**

