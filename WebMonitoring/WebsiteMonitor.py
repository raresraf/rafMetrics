import json

import arrow

from constants import sample_name, sample_url, json_path
from DockerClient import DockerRunURLClient
from request_helpers import parse_request
"""Run advanced monitoring on websites including total response time."""


class WebsiteMonitor:
    def __init__(self, url, name):
        self.url = url
        self.name = name

        self.startTimes = []
        self.endTimes = []
        self.start = None
        self.end = None
        self.total_time = None
        self.total_time_seconds = 0.0

        self.request_entry = []

    def calculate_total_time(self):
        self.start = min(self.startTimes)
        self.end = max(self.endTimes)
        self.total_time = self.end - self.start
        self.total_time_seconds = self.total_time.microseconds / 1000000.0 + self.total_time.seconds

    def add_times(self, entry):
        requestStartTime = arrow.get(entry['startedDateTime'])
        requestEndTime = arrow.get(
            entry['startedDateTime']).shift(microseconds=1000 * entry['time'])
        self.startTimes.append(requestStartTime)
        self.endTimes.append(requestEndTime)

    def process_json(self):
        with open(json_path) as json_file:
            data = json.load(json_file)
            for entry in data['log']['entries']:
                self.add_times(entry)
                request_entry = parse_request(entry)
                self.request_entry.append(request_entry)

    def get_metrics(self):
        """Return a RequestEntry structure containing metrics"""
        return self.request_entry

    def run(self):
        DockerRunURLClient(self.url).run()
        self.process_json()
        self.calculate_total_time()
        self.verbose()

    def verbose(self):
        print("Start time: %s" % self.start)
        print("End time: %s" % self.end)
        print("Total time: %.3f" % self.total_time_seconds)


monitor = WebsiteMonitor(sample_url, sample_name)
monitor.run()
print(monitor.get_metrics())
