import os
import signal
from contextlib import contextmanager
from constants import DockerResults


class DockerRunURLClient():
    TIMEOUT = 60

    def __init__(self, url):
        self.url = url
        self.status = DockerResults.STARTED

    def run(self):
        self.status = DockerResults.FAILED
        with timeout(self.TIMEOUT):
            os.system(
                "docker run -v $(pwd)/output:/output ccarpita/speedprofile-chrome \"$@\" %s"
                % self.url)
            self.status = DockerResults.SUCCESS


@contextmanager
def timeout(time):
    # Register a function to raise a TimeoutError on the signal.
    signal.signal(signal.SIGALRM, raise_timeout)
    # Schedule the signal to be sent after ``time``.
    signal.alarm(time)

    try:
        yield
    except TimeoutError:
        pass
    finally:
        # Unregister the signal so it won't be triggered
        # if the timeout is not reached.
        signal.signal(signal.SIGALRM, signal.SIG_IGN)


def raise_timeout(signum, frame):
    raise TimeoutError
