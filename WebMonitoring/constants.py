url = 'https://github.com/raresraf/rafMetrics/projects/1'
json_path = 'output/har.json'


class MonitoringStatus:
    WAITING = 'waiting'
    START = 'start'
    QUEUE = 'queue'
    PROGRESS = 'progress'
    DONE = 'done'
    FAILED = 'failed'


class RequestTypes:
    GET = 'GET'
    POST = 'POST'
