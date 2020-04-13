import json
import os

import arrow
import time

from WebMonitoring.WebsiteMonitorHelpers.request_helpers import parse_request
from WebMonitoring.clients.SpeedprofileClient import SpeedprofileClient
from WebMonitoring.configs.constants import sample_url, sample_name, DockerResults
from WebMonitoring.configs.settings import SHOW_VERBOSE_MESSAGE, json_path
"""Run advanced monitoring on websites including total response time."""


class WebsiteMonitor:
    def __init__(self, url, name):
        self.url = url
        self.name = name

        # Get current timestamp
        self.timestamp = time.localtime()

        self.startTimes = []
        self.endTimes = []
        self.start = None
        self.end = None
        self.total_time = None
        self.total_time_seconds = 0.0

        # List of RequestEntry structures, containing metrics
        self.request_entry = []

        self.docker = None

    def calculate_total_time(self):
        """Calculate total requests time as difference between last recorded response and
        first request recorded time"""

        if not self.startTimes or not self.request_entry:
            # Return -1 if there are no start times recorded or requests entries
            self.total_time_seconds = -1
            return

        self.start = min(self.startTimes)
        self.end = max(self.endTimes)
        self.total_time = self.end - self.start

        self.total_time_seconds = (self.total_time.microseconds / 1000000.0 +
                                   self.total_time.seconds +
                                   self.total_time.days * 86400)

    def add_times(self, entry):
        """Calculate a total request time as startedDateTime + time"""
        requestStartTime = arrow.get(entry["startedDateTime"])
        requestEndTime = arrow.get(
            entry["startedDateTime"]).shift(microseconds=1000 * entry["time"])
        self.startTimes.append(requestStartTime)
        self.endTimes.append(requestEndTime)

    def process_json(self):
        # Check existence of output file
        if not os.path.isfile(json_path):
            return

        # If file has been generated, proceed to parsing
        with open(json_path, encoding="utf-8") as json_file:
            data = json.load(json_file)
            for entry in data["log"]["entries"]:
                self.add_times(entry)
                request_entry = parse_request(entry)
                self.request_entry.append(request_entry)

        # Remove file after processing
        os.remove(json_path)

    def get_metrics(self):
        """Return a list of RequestEntry structures containing metrics"""
        return self.request_entry

    def run(self):
        """Generate timestamp at beginning of script"""
        self.timestamp = time.localtime()

        # Run the docker client containing the Chrome browser and export the HAR file
        self.docker = SpeedprofileClient(self.url)
        self.docker.run()

        if SHOW_VERBOSE_MESSAGE:
            print("Docker run status: " + self.docker.status)

        self.process_json()
        self.calculate_total_time()
        self.verbose()

        return self.docker.status

    def verbose(self):
        if SHOW_VERBOSE_MESSAGE:
            print("Start time: %s" % self.start)
            print("End time: %s" % self.end)
            print("Total time: %.3f" % self.total_time_seconds)

    def get_timestamp(self):
        """Return the timestamp corresponding to the execution time of the command"""
        return self.timestamp

    def get_total_time_seconds(self):
        """Return the total time for all requests processing"""
        return self.total_time_seconds


# Driver for WebsiteMonitor class
if __name__ == "__main__":
    monitor = WebsiteMonitor(sample_url, sample_name)
    monitor_result = monitor.run()

    # Check docker exit code
    if monitor_result == DockerResults.SUCCESS:
        print(monitor.get_metrics())
        print(monitor.get_timestamp())
        print(monitor.get_total_time_seconds())
