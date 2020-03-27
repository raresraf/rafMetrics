FROM ubuntu:18.04 as builder

COPY . /rafMetrics
WORKDIR /rafMetrics

RUN apt-get clean \
    && apt-get -y update

RUN apt-get install -y nodejs npm

RUN npm install -g npm@latest
RUN npm install --prefix metricsUI/ metricsUI/
RUN npm run-script --prefix metricsUI/ build


FROM nginx:1.17
COPY --from=builder /rafMetrics/metricsUI/build/ /usr/share/nginx/html
