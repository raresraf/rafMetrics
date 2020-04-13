from WebMonitoring.configs.settings import SHOW_VERBOSE_MESSAGE


def parse_request(entry):
    serverIPAddress = get_server_ip(entry)
    pageRef = get_page_ref(entry)
    startedDateTime = get_started_date_time(entry)
    time = get_time(entry)
    responseStatus = get_response_status(entry)
    headersSize = get_headers_size(entry)
    bodySize = get_body_size(entry)

    timing = get_timing(entry)
    request_entry = RequestEntry(
        serverIPAddress,
        pageRef,
        startedDateTime,
        time,
        responseStatus,
        headersSize,
        bodySize,
        timing,
    )
    request_entry.verbose()
    return request_entry


def get_timing(entry):
    return entry.get("timings", {})


def get_server_ip(entry):
    return entry.get("serverIPAddress", "")


def get_page_ref(entry):
    return entry.get("pageref", "")


def get_started_date_time(entry):
    return entry.get("startedDateTime", "")


def get_time(entry):
    return entry.get("time", "")


def get_response_status(entry):
    return entry.get("response", {}).get("status", "")


def get_headers_size(entry):
    return entry.get("response", {}).get("headersSize", "")


def get_body_size(entry):
    return entry.get("response", {}).get("bodySize", "")


class RequestEntry:
    def __init__(
        self,
        serverIPAddress,
        pageRef,
        startedDateTime,
        time,
        responseStatus,
        headersSize,
        bodySize,
        timing,
    ):
        self.serverIPAddress = serverIPAddress
        self.pageRef = pageRef
        self.startedDateTime = startedDateTime
        self.time = time
        self.responseStatus = responseStatus
        self.headersSize = headersSize
        self.bodySize = bodySize
        self.timing = TimingEntry(timing)

    def get(self):
        return self

    def verbose(self):
        if SHOW_VERBOSE_MESSAGE:
            print("serverIPAddress: %s" % self.serverIPAddress)
            print("pageRef: %s" % self.pageRef)
            print("startedDateTime: %s" % self.startedDateTime)
            print("time: %d" % self.time)
            print("responseStatus: %d" % self.responseStatus)
            print("headersSize: %d" % self.headersSize)
            print("bodySize: %d" % self.bodySize)
            self.timing.verbose()


class TimingEntry:
    def __init__(self, timing):
        self.timing = self.parse_timing(timing)

    def parse_timing(self, timing):
        self.receive = timing.get("receive", "")
        self.send = timing.get("send", "")
        self.ssl = timing.get("ssl", "")
        self.connect = timing.get("connect", "")
        self.dns = timing.get("dns", "")
        self.blocked = timing.get("blocked", "")
        self.wait = timing.get("wait", "")

    def get(self):
        return self

    def verbose(self):
        if SHOW_VERBOSE_MESSAGE:
            print("receive: %d" % self.receive)
            print("send: %d" % self.send)
            print("ssl: %d" % self.ssl)
            print("connect: %d" % self.connect)
            print("dns: %d" % self.dns)
            print("blocked: %d" % self.blocked)
            print("wait: %d" % self.wait)
