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

# jsonify a Decimal
RUN pip3 install simplejson

# Debugging
RUN pip3 install ipython
RUN pip3 install flask-shell-ipython


COPY . /rafMetrics
WORKDIR /rafMetrics

EXPOSE 5000:5000

ENV PYTHONPATH="/rafMetrics"
ENTRYPOINT ["python3", "./Login/app.py"]

# For development purpose only
# ENTRYPOINT ["tail", "-f", "/dev/null"]

