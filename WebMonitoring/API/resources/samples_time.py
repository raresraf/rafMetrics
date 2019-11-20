def resources_get_samples_time_daily(mysql):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "select ResponseTime from PING where Resourceid = %s order by Timestamp desc limit 7;"
            % (resource_name))
        rows = cursor.fetchall()
        return rows
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

    result = []
    for i in range(24):
        result.append({'custom_data': i})
    return result


def resources_get_samples_time_weekly(mysql):
    result = []
    for i in range(7):
        result.append({'custom_data': i})
    return result


def resources_get_samples_time_monthly(mysql):
    result = []
    for i in range(30):
        result.append({'custom_data': i})
    return result
