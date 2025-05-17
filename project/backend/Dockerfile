FROM python:3.12-slim

WORKDIR /app
ENV POETRY_VIRTUALENVS_IN_PROJECT=true

# Sistem bağımlılıkları
RUN apt-get update && apt-get install -y build-essential curl libpq-dev

# Poetry kur
RUN curl -sSL https://install.python-poetry.org | python3 -

ENV PATH="/root/.local/bin:$PATH"

# pyproject.toml ve lock dosyası
# COPY pyproject.toml poetry.lock ./
COPY req.txt ./
# RUN poetry install --no-root || poetry install
# RUN poetry install
# RUN pip install -U poetry
# Bağımlılıkları kur

# Uygulama dosyaları
# RUN poetry config virtualenvs.create false && poetry install --no-dev
COPY . .
# RUN poetry add gunicorn
RUN pip install -r req.txt
RUN pip install gunicorn
# CMD ["poetry", "run", "gunicorn", "config.product.wsgi:application", "--bind", "0.0.0.0:8000"]
# CMD ["DJANGO_SETTINGS_MODULE=config.settings.product", "poetry", "run", "gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]
# COPY entrypoint.sh ./entrypoint.sh
# RUN chmod a+x ./entrypoint.sh

# ENTRYPOINT ["./entrypoint.sh"]

CMD ["DJANGO_SETTINGS_MODULE=config.settings.product", "gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]


