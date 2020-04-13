import os

# Set SHOW_VERBOSE_MESSAGE on true for multiple logs of the monitoring tools
SHOW_VERBOSE_MESSAGE = False

# Set SHOW_PROGRESS_MESSAGE on true for general logs about current process (used in ResourceMonitoring)
SHOW_PROGRESS_MESSAGE = True

# Default speedprofile script location inside repo
# Original speedprofile code: https://github.com/parasdahal/speedprofile
SPEEDPROFILE_LOCATION = "./WebMonitoring/WebsiteMonitorHelpers/entrypoint.sh"

# Define the sample time between two consecutive monitorings
SAMPLE_TIME = 3600

# JSON output location
json_path = "./output/har.json"

# MySQL DB configs
MYSQL_DATABASE_USER = "root"
MYSQL_DATABASE_PASSWORD = "password"
MYSQL_DATABASE_DB = "WebMonitoring"
if os.environ.get("DOCKER_COMPOSE_BUILD"):
    MYSQL_DATABASE_HOST = "mysql"
else:
    MYSQL_DATABASE_HOST = "10.96.0.2"
