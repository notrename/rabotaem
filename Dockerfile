FROM python:3.9-slim

COPY . /app
WORKDIR /app

ENV driver_type='docker'
RUN pip install --no-cache-dir -r requirements.txt
