FROM python:3.9-slim

RUN apt-get update && apt-get install -y build-essential libfreetype6-dev libjpeg-dev libopenjp2-7 libtiff5

RUN pip3 install poetry

WORKDIR /app
COPY src/pyproject.toml src/poetry.lock /app/
RUN poetry config virtualenvs.create false \
      && poetry install --no-dev --no-interaction --no-ansi

COPY src .
