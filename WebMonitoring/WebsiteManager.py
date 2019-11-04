import time

from constants import ResourceEntry, RequestTypes, resources, DockerResults
from WebsiteMonitor import WebsiteMonitor
import mysql.connector


class WebsiteManager:
    def __init__(self, sample_time=86400):
        self.sample_time = sample_time
        self.websites = []
        self.cnx = None

    def run(self):
        for (website_url, website_name) in self.websites:
            monitor = WebsiteMonitor(website_url, website_name)
            monitor_result = monitor.run()

            # Check docker exit code
            if monitor_result == DockerResults.SUCCESS:
                print(monitor.get_metrics())
                print(monitor.get_timestamp())
                print(monitor.get_total_time_seconds())

    def start(self):
        # Connect to DB
        self.cnx = mysql.connector.connect(user='root',
                                           password='password',
                                           host='10.96.0.2',
                                           database='WebMonitoring')

        while True:
            self.websites = []

            # Check for any update in the list of websites
            cursor = self.cnx.cursor(buffered=True)
            query = ('SELECT WebsiteUrl, WebsiteName from WEBSITES')
            cursor.execute(query)

            for (website_url, website_name) in cursor:
                self.websites.append((website_url, website_name))

            self.run()
            time.sleep(self.sample_time)


WebsiteManager(86400).start()