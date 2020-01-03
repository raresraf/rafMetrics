# Set SHOW_VERBOSE_MESSAGE on true for multiple logs of the monitoring tools
SHOW_VERBOSE_MESSAGE = False

# Default speedprofile script location inside repo
# Original speedprofile code: https://github.com/parasdahal/speedprofile
SPEEDPROFILE_LOCATION = './WebMonitoring/WebsiteMonitorHelpers/entrypoint.sh'

# Define the sample time between two consecutive monitorings
SAMPLE_TIME = 3600

# JSON output location
json_path = './output/har.json'

# MySQL DB configs
MYSQL_DATABASE_USER = 'root'
MYSQL_DATABASE_PASSWORD = 'password'
MYSQL_DATABASE_DB = 'WebMonitoring'
MYSQL_DATABASE_HOST = '10.96.0.2'
