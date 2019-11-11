FROM python:3.6-slim

RUN apt-get clean \
    && apt-get -y update

RUN apt-get -y install \
    nginx \
    python3-dev \
    build-essential

WORKDIR /app

COPY app.py /app/app.py
COPY startup.sh /app/startup.sh

RUN chmod +x ./startup.sh

EXPOSE 80
CMD [ "./startup.sh" ]
