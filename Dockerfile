FROM python:3.8.0-alpine3.10

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN apk add --update \
    curl \
    && rm -rf /var/cache/apk/*

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./run.py" ]
