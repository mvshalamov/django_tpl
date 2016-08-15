FROM python:3.5.1

ADD requirements.txt .
RUN pip install -r requirements.txt
ADD . /code
WORKDIR /code
RUN python manage.py collectstatic --no-input
