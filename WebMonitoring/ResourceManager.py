import time

from ResourceMonitor import ResourceMonitor
from constants import resources


class ResourceManager:
    def __init__(self, sample_time=86400):
        self.sample_time = sample_time

    def run(self):
        for resource in resources:
            monitor = ResourceMonitor(resource.resource_url,
                                      requestType=resource.resource_command,
                                      requestPayload=resource.resource_payload)
            monitor.run()
            print(monitor.get_metrics())

    def start(self):
        while True:
            self.run()
            time.sleep(self.sample_time)


ResourceManager(10).start()
