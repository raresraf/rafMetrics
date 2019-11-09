import time

import mysql.connector

from WebsiteMonitor import WebsiteMonitor
from constants import DockerResults


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

                cursor = self.cnx.cursor(buffered=True)
                query = (
                    'SELECT Websiteid, WebsiteName from WEBSITES where WebsiteUrl = \'%s\''
                    % website_url)
                cursor.execute(query)

                # Get Websiteid
                for (website_id, website_name) in cursor:
                    query = (
                        ('INSERT INTO WEBSITES_METRICS(Websiteid, TotalTime) '
                         'VALUES (%d, %lf)') %
                        (website_id, monitor.get_total_time_seconds()))
                    cursor_insert = self.cnx.cursor(buffered=True)
                    # Insert new Website Metric Entry in DB
                    cursor_insert.execute(query)
                    self.cnx.commit()

                    cursor_metric_id = self.cnx.cursor(buffered=True)
                    query = (
                        'select max(Metricid) from WEBSITES_METRICS where Websiteid = %d'
                        % website_id)
                    cursor_metric_id.execute(query)

                    # Get Metricid
                    for (metric_id, ) in cursor_metric_id:
                        for request in monitor.request_entry:
                            query = ((
                                'INSERT INTO REQUESTS(Metricid, serverIPAddress, pageRef, startedDateTime, time, responseStatus, headersSize, bodySize) '
                                'VALUES (%d, \'%s\', \'%s\', \'%s\', %d, %d, %d, %d )'
                            ) % (metric_id, request.serverIPAddress,
                                 request.pageRef, request.startedDateTime,
                                 request.time, request.responseStatus,
                                 request.headersSize, request.bodySize))
                            cursor_insert_request = self.cnx.cursor(
                                buffered=True)
                            # Insert new timing in DB
                            cursor_insert_request.execute(query)
                            self.cnx.commit()

                            cursor_request_id = self.cnx.cursor(buffered=True)
                            query = (
                                'select max(Requestid) from REQUESTS where Metricid = %d '
                                % metric_id)
                            cursor_request_id.execute(query)

                            # Get Requestid
                            for (request_id, ) in cursor_request_id:
                                timing = request.timing
                                cursor_insert_timing = self.cnx.cursor(
                                    buffered=True)
                                query = (
                                    'INSERT INTO TIMINGS(Requestid, Receive, Send, SSLTime, Connect, DNS, Blocked, Wait) VALUES (%d, %d, %d, %d, %d, %d, %d, %d)'
                                    %
                                    (request_id, request.timing.receive,
                                     timing.send, timing.ssl, timing.connect,
                                     timing.dns, timing.blocked, timing.wait))
                                # Insert new timing in DB
                                cursor_insert_timing.execute(query)
                                self.cnx.commit()

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


WebsiteManager(3600).start()
