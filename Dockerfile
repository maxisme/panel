FROM python:3.9-slim
RUN apt-get update && apt-get install -y build-essential libfreetype6-dev libjpeg-dev libopenjp2-7 libtiff5 libffi-dev openssl libssl-dev
RUN pip install --upgrade pip
RUN pip install cryptography==2.3
RUN pip install poetry

WORKDIR /app

COPY src/poetry.lock src/pyproject.toml /app/
ENV CFLAGS=-fcommon
RUN poetry env use system
RUN poetry config virtualenvs.create false
RUN poetry install

COPY src .

#RUN export PYTHONPATH="${PYTHONPATH}:/app/panel/"
