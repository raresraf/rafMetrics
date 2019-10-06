import os


class DockerRunURLClient():
    def __init__(self, url):
        self.url = url

    def run(self):
        os.system(
            "docker run -v $(pwd)/output:/output ccarpita/speedprofile-chrome \"$@\" %s"
            % self.url)
