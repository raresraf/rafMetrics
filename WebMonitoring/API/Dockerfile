FROM python:3.6-slim

RUN apt-get clean \
    && apt-get -y update

RUN apt-get -y install \
    nginx \
    python3-dev \
    build-essential 

WORKDIR /app

RUN pip3 install pymysql
RUN pip3 install flask
RUN pip3 install flask-mysql
RUN pip3 install flask-cors

COPY . /app

EXPOSE 5000:5000

ENTRYPOINT ["python3", "app.py"]
#ENTRYPOINT ["tail", "-f", "/dev/null"]
