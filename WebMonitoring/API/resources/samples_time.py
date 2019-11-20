def resources_get_samples_time_daily(mysql):
    result = []
    for i in range(7):
        result.append({'custom_data': i})
    return result


def resources_get_samples_time_weekly(mysql):
    result = []
    for i in range(4):
        result.append({'custom_data': i})
    return result


def resources_get_samples_time_monthly(mysql):
    result = []
    for i in range(30):
        result.append({'custom_data': i})
    return result
