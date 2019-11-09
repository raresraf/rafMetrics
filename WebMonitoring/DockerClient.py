import os
import signal
from contextlib import contextmanager

from constants import DockerResults


class DockerRunURLClient():
    """
    ACTUAL:
    DockerRunURLClient executes entrypoint.sh script

    DEPRECATED:
    DockerRunURLClient class receives a URL and runs a new docker
    with https://github.com/parasdahal/speedprofile image
    and helps capture HTTP Archive (HAR) and additional performance data
    using Navigation Timing API from either Chrome or Firefox headlessly.
    """

    # Default timeout for docker run command
    TIMEOUT = 90

    def __init__(self, url):
        self.url = url
        self.status = DockerResults.STARTED

    def run(self):
        # Set current status to FAILED
        self.status = DockerResults.FAILED

        # Set timeout for docker run command
        with self.timeout(self.TIMEOUT):
            # Deprecated:
            #    os.system(
            #    "docker run -v $(pwd)/output:/output ccarpita/speedprofile-chrome \"$@\" %s"
            #    % self.url)
            os.system("./WebsiteMonitorHelpers/entrypoint.sh %s" % self.url)

            # If docker run command success within timeout time, set current status to SUCCESS
            self.status = DockerResults.SUCCESS

    @contextmanager
    def timeout(self, time):
        # Register a function to raise a TimeoutError on the signal.
        signal.signal(signal.SIGALRM, self.raise_timeout)
        # Schedule the signal to be sent after time.
        signal.alarm(time)

        try:
            yield
        except TimeoutError:
            pass
        finally:
            # Unregister the signal so it won't be triggered if the timeout is not reached.
            signal.signal(signal.SIGALRM, signal.SIG_IGN)

    def raise_timeout(self, signum, frame):
        raise TimeoutError
