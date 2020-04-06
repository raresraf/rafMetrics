import requests
import time

from WebMonitoring.configs.constants import MonitoringStatus, RequestTypes, sample_url
from WebMonitoring.configs.settings import SHOW_PROGRESS_MESSAGE


class ResourceMonitor:
    """Executes simple requests on a given resource. Measure total time for request response"""
    def __init__(self,
                 url,
                 timeout=10,
                 requestType=RequestTypes.GET,
                 requestPayload=None):
        self.url = url
        self.timeout = timeout
        self.status = MonitoringStatus.WAITING
        self.requestType = requestType
        self.requestPayload = requestPayload

        # Metrics returned
        self.responseTime = 0
        self.responseSize = 0
        self.timestamp = time.localtime()

    def execute_request(self):
        self.timestamp = time.localtime()
        if self.requestType == RequestTypes.GET:
            return requests.get(self.url,
                                timeout=self.timeout,
                                params=self.requestPayload)
        if self.requestType == RequestTypes.POST:
            return requests.post(self.url,
                                 timeout=self.timeout,
                                 data=self.requestPayload)

    def update_metrics(self, responseTime, responseSize):
        self.responseTime = responseTime
        self.responseSize = responseSize

    def get_metrics(self):
        """Return a tuple (responseTime, responseSize)"""
        return (self.responseTime, self.responseSize)

    def get_timestamp(self):
        """Return the timestamp corresponding to the execution time of the command"""
        return self.timestamp

    def run(self):
        try:
            self.status = MonitoringStatus.START
            r = self.execute_request()

            self.status = MonitoringStatus.PROGRESS
            elapsed_seconds = r.elapsed.total_seconds()
            size = len(r.content)
            self.update_metrics(elapsed_seconds, size)

            self.status = MonitoringStatus.DONE

        except requests.exceptions.ConnectTimeout:
            self.status = MonitoringStatus.FAILED
            self.update_metrics(-1, 0)

        except requests.exceptions.ConnectionError:
            self.status = MonitoringStatus.FAILED
            self.update_metrics(-1, 0)

        except Exception:
            self.status = MonitoringStatus.FAILED
            self.update_metrics(-1, 0)

        self.verbose()

    def verbose(self):
        if SHOW_PROGRESS_MESSAGE:
            print("%s request status: %s" % (self.requestType, self.status))
            print("URL: %s" % self.url)
            if self.status == MonitoringStatus.DONE:
                print("Request total elapsed time: %.3f s" % self.responseTime)
                print("Request size: %.2f KBytes" %
                      (self.responseSize / 1024.0))


# Sample driver for ResourceMonitor class
class DriverResourceMonitor:
    def __init__(self):
        self.sample_url = sample_url

    def run(self):
        monitor = ResourceMonitor(sample_url)
        monitor.run()
        print(monitor.get_metrics())
