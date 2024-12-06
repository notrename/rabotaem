FROM python:3.9-slim

ENV driver_type='docker'

COPY . /app
WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["pytest", "tests/"]