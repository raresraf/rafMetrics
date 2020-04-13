import calendar
import datetime

from WebMonitoring.API.constants import PERIOD


def get_timestamp_query(period, i, start):
    if period.lower() == PERIOD.DAILY:
        return (start + i) % 24
    if period.lower() == PERIOD.WEEKLY:
        return (start + 6 * i) % 24
    if period.lower() == PERIOD.MONTHLY:
        today = datetime.date.today()
        first = today.replace(day=1)
        lastMonth = first - datetime.timedelta(days=1)
        modulo = calendar.monthrange(lastMonth.year, lastMonth.month)[1]
        return (start + i - 1) % modulo + 1
