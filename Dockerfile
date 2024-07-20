FROM python:3.9-slim

RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/
COPY company_nginx.conf /etc/nginx/conf.d/default.conf
COPY company/uwsgi_params /etc/nginx/uwsgi_params

RUN python manage.py collectstatic --noinput

CMD ["sh", "-c", "uwsgi --ini /app/company/uwsgi.ini"]
