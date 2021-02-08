FROM python:3.9-slim
RUN apt-get update && apt-get install -y build-essential libfreetype6-dev libjpeg-dev libopenjp2-7 libtiff5 libffi-dev

WORKDIR /app
COPY src/requirements.txt /app/
RUN pip3 install -r requirements.txt

COPY src .
