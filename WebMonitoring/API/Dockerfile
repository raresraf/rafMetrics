FROM python:3.6-slim

RUN apt-get clean \
    && apt-get -y update

RUN apt-get -y install \
    nginx \
    python3-dev \
    build-essential

COPY . /rafMetrics
WORKDIR /rafMetrics

# Install requirements for Python modules
RUN pip3 install -r requirements.txt

EXPOSE 5000:5000

ENV PYTHONPATH="/rafMetrics"
ENTRYPOINT ["python3", "./WebMonitoring/API/app.py"]

# For development purpose only
# ENTRYPOINT ["tail", "-f", "/dev/null"]
