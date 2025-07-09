FROM python:3.13-slim-bullseye

RUN apt-get update && \
    apt-get install -y build-essential libpq-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN adduser --disabled-password --no-create-home django

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    DJANGO_SETTINGS_MODULE=config.settings.product \
    POETRY_VIRTUALENVS_IN_PROJECT=true

COPY requirements.latest.txt ./

RUN pip install --no-cache-dir -r requirements.latest.txt && \
    pip install --no-cache-dir gunicorn

COPY . .

USER django

EXPOSE 1000

CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:1000"]
