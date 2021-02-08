FROM python:3.9-slim

RUN apt-get update && apt-get install -y build-essential libfreetype6-dev libjpeg-dev libopenjp2-7 libtiff5 libffi-dev curl

RUN curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python3

WORKDIR /app
COPY src/pyproject.toml src/poetry.lock /app/
RUN poetry config virtualenvs.create false \
      && poetry install --no-dev --no-interaction --no-ansi

COPY src .
