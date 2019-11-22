FROM python:3.6-slim

RUN apt-get clean \
    && apt-get -y update

RUN apt-get -y install \
    nginx \
    python3-dev \
    build-essential 

RUN pip3 install pymysql
RUN pip3 install flask
RUN pip3 install flask-mysql
RUN pip3 install flask-cors


COPY . /rafMetrics
WORKDIR /rafMetrics

EXPOSE 5000:5000

ENV PYTHONPATH="/rafMetrics"
ENTRYPOINT ["python3", "./WebMonitoring/API/app.py"]

# For development purpose only
# ENTRYPOINT ["tail", "-f", "/dev/null"]
