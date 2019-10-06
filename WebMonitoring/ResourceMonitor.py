import requests

from constants import MonitoringStatus, RequestTypes
from constants import url


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
        """Metrics returned"""
        self.responseTime = 0
        self.responseSize = 0

    def execute_request(self):
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

        self.verbose()

    def verbose(self):
        print("%s request status: %s" % (self.requestType, self.status))
        print("URL: %s" % self.url)
        if self.status == MonitoringStatus.DONE:
            print("Request total elapsed time: %.3f s" % self.responseTime)
            print("Request size: %.2f KBytes" % (self.responseSize / 1024.0))


ResourceMonitor(url).run()