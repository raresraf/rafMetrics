import subprocess

from WebMonitoring.configs.constants import DockerResults
from WebMonitoring.configs.settings import SPEEDPROFILE_LOCATION


class SpeedprofileClient:
    """
    Client for https://github.com/parasdahal/speedprofile


    ACTUAL:
    SpeedprofileClient executes entrypoint.sh script

    DEPRECATED:
    SpeedprofileClient class receives a URL and runs a new docker
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

        # Deprecated:
        #    os.system(
        #    "docker run -v $(pwd)/output:/output ccarpita/speedprofile-chrome \"$@\" %s"
        #    % self.url)
        try:
            subprocess.call("%s %s" % (SPEEDPROFILE_LOCATION, self.url),
                            shell=True,
                            timeout=90)
            self.status = DockerResults.SUCCESS
        except subprocess.TimeoutExpired:
            self.status = DockerResults.FAILED
        finally:
            pass
