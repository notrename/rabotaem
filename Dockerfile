FROM python:3.9-slim

RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    && apt-get clean

RUN apt-get install -y \
    chromium \
    chromium-driver \
    && apt-get clean

RUN wget https://dl.bintray.com/qameta/generic/allure/2.15.0/allure-2.15.0.tgz \
    && tar -zxvf allure-2.15.0.tgz -C /opt/ \
    && ln -s /opt/allure-2.15.0/bin/allure /usr/bin/allure \
    && rm allure-2.15.0.tgz

COPY . /app
WORKDIR /app

ENV driver_type='docker'
ENV CHROME_BIN=/usr/bin/chromium
ENV CHROME_DRIVER=/usr/bin/chromium-driver

RUN pip install --no-cache-dir -r requirements.txt

CMD ["sh", "-c", "pytest --alluredir=allure-results && allure generate allure-results --clean -o allure-report"]