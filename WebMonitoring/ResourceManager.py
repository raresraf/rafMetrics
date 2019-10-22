import time

from ResourceMonitor import ResourceMonitor
from constants import ResourceEntry, RequestTypes, resources

import mysql.connector


class ResourceManager:
    def __init__(self, sample_time=86400):
        self.sample_time = sample_time
        self.resources = []
        self.cnx = None

    def run(self):
        for resource in self.resources:
            monitor = ResourceMonitor(resource.resource_url,
                                      requestType=resource.resource_command,
                                      requestPayload=resource.resource_payload)
            monitor.run()
            print(monitor.get_metrics())

            cursor = self.cnx.cursor(buffered=True)
            query = (
                'SELECT ResourceId from RESOURCE where ResourceName = \'%s\'' %
                resource.resource_url)
            cursor.execute(query)

            resourceId = 1
            for resource_id in cursor:
                resourceId = resource_id[0]

            query = (
                ('INSERT INTO PING(Resourceid, ResponseTime, ResponseSize) '
                 'VALUES (%d, %lf, %d)') %
                (resourceId, monitor.get_metrics()[0],
                 monitor.get_metrics()[1]))

            cursor.execute(query)
            self.cnx.commit()

    def start(self):

        self.cnx = mysql.connector.connect(user='root',
                                           password='password',
                                           host='10.96.0.2',
                                           database='WebMonitoring')
        cursor = self.cnx.cursor(buffered=True)
        query = ('SELECT ResourceName, Command from RESOURCE where Userid = 1')
        cursor.execute(query)

        for (resouce_name, command) in cursor:
            if command == RequestTypes.GET:
                self.resources.append(
                    ResourceEntry(resouce_name, resouce_name, RequestTypes.GET,
                                  None))
            elif command.contains(RequestTypes.POST):
                self.resources.append(
                    # TODO : Parse payload
                    ResourceEntry(resouce_name, resouce_name,
                                  RequestTypes.POST, None))

        while True:
            self.run()
            time.sleep(self.sample_time)


ResourceManager(1200).start()
