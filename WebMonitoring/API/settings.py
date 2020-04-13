import os

# DB configs
MYSQL_DATABASE_USER = "root"
MYSQL_DATABASE_PASSWORD = "password"
MYSQL_DATABASE_DB = "WebMonitoring"
if os.environ.get("DOCKER_COMPOSE_BUILD"):
    MYSQL_DATABASE_HOST = "mysql"
else:
    MYSQL_DATABASE_HOST = "10.96.0.2"
