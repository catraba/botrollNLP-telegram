FROM python:3.10.6-slim-buster

EXPOSE 80

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

COPY requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /app
COPY . /app

CMD ["gunicorn", "--certfile", "mycert.pem",  "--keyfile",  "mykey.key", "--ssl-version", "TLSv1_2", "--bind", "0.0.0.0:80", "app:app"]