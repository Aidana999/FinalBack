FROM python:3.8

RUN set -ex && mkdir /app
WORKDIR /app

COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY . /app

CMD python manage.py makemigrations && python manage.py migrate && python manage.py collectstatic --no-input && gunicorn -w 3 -b 0.0.0.0:80 testProject.wsgi