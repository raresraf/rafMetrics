SAMPLE_DOCKER_COMPOSE = """version: "3.3"

# docker stack deploy -c docker_config/docker-compose.yaml rafMetrics
services:
  # docker build -f mysql_config/Dockerfile -t raresraf/rafmetricsmysql:latest .
  mysql:
    image: raresraf/rafmetricsmysql:latest
    environment:
      DOCKER_COMPOSE_BUILD: "true"
    ports:
      - "3306:3306"
    # expose:
    #  - '3306'
    networks:
      - backend
    volumes:
      - db-volume:/var/lib/mysql
    deploy:
      replicas: 1
      placement:
        constraints: [node.role == manager]

  # docker build -f WebMonitoring/DockerfileResource -t raresraf/resourcemonitor:latest .
  resourcemonitor:
    image: raresraf/resourcemonitor:latest
    depends_on:
      - mysql
    environment:
      DOCKER_COMPOSE_BUILD: "true"
    networks:
      - backend
    deploy:
      replicas: 1
      placement:
        constraints: [node.role == worker]

  # docker build -f WebMonitoring/DockerfileWebsite -t raresraf/websitemonitor:latest .
  websitemonitor:
    image: raresraf/websitemonitor:latest
    depends_on:
      - mysql
    environment:
      DOCKER_COMPOSE_BUILD: "true"
    networks:
      - backend
    deploy:
      replicas: 1
      placement:
        constraints: [node.role == worker]

  login:
    image: raresraf/login:latest
    depends_on:
      - mysql
    environment:
      DOCKER_COMPOSE_BUILD: "true"
    ports:
      - "31001:5000"
    networks:
      - backend
      - frontend
    deploy:
      replicas: 1
      placement:
        constraints: [node.role == worker]

  webmonitoringapi:
    image: raresraf/webmonitoringapi:latest
    depends_on:
      - mysql
    environment:
      DOCKER_COMPOSE_BUILD: "true"
    ports:
      - "31002:5000"
    networks:
      - backend
      - frontend
    deploy:
      replicas: 2
      placement:
        constraints: [node.role == worker]

  # docker build -f metricsUI/Dockerfile -t raresraf/metricsui:latest .
  metricsui:
    image: raresraf/metricsui:latest
    depends_on:
      - webmonitoringapi
      - login
    environment:
      DOCKER_COMPOSE_BUILD: "true"
    ports:
      - "31000:80"
    networks:
      - frontend
    deploy:
      replicas: 2
      placement:
        constraints: [node.role == worker]

  visualizer:
    image: dockersamples/visualizer:stable
    ports:
      - "8080:8080"
    stop_grace_period: 1m30s
    volumes:
      - "/var/run/docker.sock:/var/run/docker.sock"
    deploy:
      replicas: 1
      placement:
        constraints: [node.role == manager]

  grafana:
    image: grafana/grafana:latest
    ports:
      - "32001:3000"
    depends_on:
      - mysql
    environment:
      - "GF_SECURITY_ADMIN_USER=TestUsername"
      - "GF_SECURITY_ADMIN_PASSWORD=TestUsername"
    user: "0"
    networks:
      - backend
    deploy:
      replicas: 1
      placement:
        constraints: [node.role == worker]

volumes:
  db-volume:

networks:
  backend:
  frontend:
"""

EXPECTED_DOCKER_COMPOSE = """networks:
  backend: null
  frontend: null
services:
  grafana:
    depends_on:
    - mysql
    deploy:
      replicas: 1
    environment:
    - GF_SECURITY_ADMIN_USER=TestUsername
    - GF_SECURITY_ADMIN_PASSWORD=TestUsername
    image: grafana/grafana:latest
    networks:
    - backend
    ports:
    - 32001:3000
    user: '0'
  login:
    depends_on:
    - mysql
    deploy:
      replicas: 1
    environment:
      DOCKER_COMPOSE_BUILD: 'true'
    image: raresraf/login:latest
    networks:
    - backend
    - frontend
    ports:
    - 31001:5000
  metricsui:
    depends_on:
    - webmonitoringapi
    - login
    deploy:
      replicas: 2
    environment:
      DOCKER_COMPOSE_BUILD: 'true'
    image: raresraf/metricsui:latest
    networks:
    - frontend
    ports:
    - 31000:80
  mysql:
    deploy:
      replicas: 1
    environment:
      DOCKER_COMPOSE_BUILD: 'true'
    image: raresraf/rafmetricsmysql:latest
    networks:
    - backend
    ports:
    - 3306:3306
    volumes:
    - db-volume:/var/lib/mysql
  resourcemonitor:
    depends_on:
    - mysql
    deploy:
      replicas: 1
    environment:
      DOCKER_COMPOSE_BUILD: 'true'
    image: raresraf/resourcemonitor:latest
    networks:
    - backend
  visualizer:
    deploy:
      replicas: 1
    image: dockersamples/visualizer:stable
    ports:
    - 8080:8080
    stop_grace_period: 1m30s
    volumes:
    - /var/run/docker.sock:/var/run/docker.sock
  webmonitoringapi:
    depends_on:
    - mysql
    deploy:
      replicas: 2
    environment:
      DOCKER_COMPOSE_BUILD: 'true'
    image: raresraf/webmonitoringapi:latest
    networks:
    - backend
    - frontend
    ports:
    - 31002:5000
  websitemonitor:
    depends_on:
    - mysql
    deploy:
      replicas: 1
    environment:
      DOCKER_COMPOSE_BUILD: 'true'
    image: raresraf/websitemonitor:latest
    networks:
    - backend
version: '3.3'
volumes:
  db-volume: null
"""
