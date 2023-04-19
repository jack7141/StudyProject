FROM python:3.8
MAINTAINER Jun Park <jpark4395@fount.co>

RUN apt-get update \
    && apt-get install -y redis-tools

WORKDIR /app
COPY . /app
RUN pip3 install -r requirements.txt
