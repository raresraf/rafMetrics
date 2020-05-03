import mysql.connector
import time

from WebMonitoring.configs.constants import ResourceEntry, RequestTypes
from WebMonitoring.configs.settings import (
    SAMPLE_TIME,
    MYSQL_DATABASE_USER,
    MYSQL_DATABASE_PASSWORD,
    MYSQL_DATABASE_HOST,
    MYSQL_DATABASE_DB,
)
from WebMonitoring.monitors.ResourceMonitor import ResourceMonitor


class ResourceManager:
    def __init__(self, sample_time=3600):
        self.sample_time = sample_time
        self.resources = []
        self.cnx = None

    def run(self):
        for resource in self.resources:

            monitor = ResourceMonitor(
                resource.resource_url,
                requestType=resource.resource_command,
                requestPayload=resource.resource_payload,
            )
            monitor.run()

            cursor = self.cnx.cursor(buffered=True)
            query = (
                "SELECT Resourceid, ResourceName from RESOURCE where ResourceName = '%s'"
                % resource.resource_url)
            cursor.execute(query)

            for (resource_id, _) in cursor:
                query = (
                    "INSERT INTO PING(Resourceid, ResponseTime, ResponseSize) "
                    "VALUES (%d, %lf, %d)") % (resource_id,
                                               monitor.get_metrics()[0],
                                               monitor.get_metrics()[1])
                cursor_insert = self.cnx.cursor(buffered=True)
                cursor_insert.execute(query)
                self.cnx.commit()

    def start(self):
        # Connect to DB
        self.cnx = mysql.connector.connect(
            user=MYSQL_DATABASE_USER,
            password=MYSQL_DATABASE_PASSWORD,
            host=MYSQL_DATABASE_HOST,
            database=MYSQL_DATABASE_DB,
        )

        while True:
            self.resources = []

            # Check for any update in the list of resources
            cursor = self.cnx.cursor(buffered=True)
            query = "SELECT ResourceName, Command from RESOURCE"
            cursor.execute(query)

            for (resource_name, command) in cursor:
                if command == RequestTypes.GET:
                    self.resources.append(
                        ResourceEntry(resource_name, resource_name,
                                      RequestTypes.GET, None))
                elif command.contains(RequestTypes.POST):
                    self.resources.append(
                        # TODO : Parse payload
                        ResourceEntry(resource_name, resource_name,
                                      RequestTypes.POST, None))

            self.run()
            time.sleep(self.sample_time)


if __name__ == "__main__":
    ResourceManager(SAMPLE_TIME).start()
