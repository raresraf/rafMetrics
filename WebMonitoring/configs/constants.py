class MonitoringStatus:
    WAITING = "waiting"
    START = "start"
    QUEUE = "queue"
    PROGRESS = "progress"
    DONE = "done"
    FAILED = "failed"


class DockerResults:
    FAILED = "failed"
    SUCCESS = "success"
    STARTED = "started"
    FINISHED = "finished"


class RequestTypes:
    GET = "GET"
    POST = "POST"


class ResourceEntry:
    def __init__(
        self,
        resource_url,
        resource_name,
        resource_command=RequestTypes.GET,
        resource_payload=None,
    ):
        self.resource_url = resource_url
        self.resource_name = resource_name
        self.resource_command = resource_command
        self.resource_payload = resource_payload


sample_url = "https://github.com/raresraf/rafMetrics/projects/1"
sample_name = "GitHub"
sample_resource_command = RequestTypes.GET
sample_resource_payload = None

sample_resource = ResourceEntry(
    sample_url,
    sample_name,
    resource_command=sample_resource_command,
    resource_payload=sample_resource_payload,
)

resources = [sample_resource]
