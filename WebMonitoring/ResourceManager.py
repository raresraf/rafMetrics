import time

import mysql.connector

from configs.constants import ResourceEntry, RequestTypes
from configs.settings import SAMPLE_TIME
from monitors.ResourceMonitor import ResourceMonitor


class ResourceManager:
    def __init__(self, sample_time=3600):
        self.sample_time = sample_time
        self.resources = []
        self.cnx = None

    def run(self):
        for resource in self.resources:

            monitor = ResourceMonitor(resource.resource_url,
                                      requestType=resource.resource_command,
                                      requestPayload=resource.resource_payload)
            monitor.run()

            cursor = self.cnx.cursor(buffered=True)
            query = (
                'SELECT Resourceid, ResourceName from RESOURCE where ResourceName = \'%s\''
                % resource.resource_url)
            cursor.execute(query)

            for (resource_id, resource_name) in cursor:
                query = ((
                    'INSERT INTO PING(Resourceid, ResponseTime, ResponseSize) '
                    'VALUES (%d, %lf, %d)') %
                         (resource_id, monitor.get_metrics()[0],
                          monitor.get_metrics()[1]))
                cursor_insert = self.cnx.cursor(buffered=True)
                cursor_insert.execute(query)
                self.cnx.commit()

    def start(self):
        # Connect to DB
        self.cnx = mysql.connector.connect(user='root',
                                           password='password',
                                           host='10.96.0.2',
                                           database='WebMonitoring')

        while True:
            self.resources = []

            # Check for any update in the list of resources
            cursor = self.cnx.cursor(buffered=True)
            query = ('SELECT ResourceName, Command from RESOURCE')
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


ResourceManager(SAMPLE_TIME).start()
