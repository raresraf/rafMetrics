from WebMonitoring.API.constants import PERIOD
from WebMonitoring.API.resources.helpers import get_timestamp_query


def resources_get_samples_size_daily(mysql, resource_name):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        """
        Compatibility warning: PEP-249 specifies that any modified
        parameters must be returned. This is currently impossible
        as they are only available by storing them in a server
        variable and then retrieved by a query. Since stored
        procedures return zero or more result sets, there is no
        reliable way to get at OUT or INOUT parameters via callproc.
        The server variables are named @_procname_n, where procname
        is the parameter above and n is the position of the parameter
        (from zero). Once all result sets generated by the procedure
        have been fetched, you can issue a SELECT @_procname_0, ...
        query using .execute() to get any OUT or INOUT values.
        """
        args = [
            resource_name, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0
        ]

        cursor.callproc('get_daily_samples_size_websites', args)
        cursor.execute("SELECT "
                       "@_get_daily_samples_size_websites_0, "
                       "@_get_daily_samples_size_websites_1, "
                       "@_get_daily_samples_size_websites_2, "
                       "@_get_daily_samples_size_websites_3, "
                       "@_get_daily_samples_size_websites_4, "
                       "@_get_daily_samples_size_websites_5, "
                       "@_get_daily_samples_size_websites_6, "
                       "@_get_daily_samples_size_websites_7, "
                       "@_get_daily_samples_size_websites_8, "
                       "@_get_daily_samples_size_websites_9, "
                       "@_get_daily_samples_size_websites_10, "
                       "@_get_daily_samples_size_websites_11, "
                       "@_get_daily_samples_size_websites_12, "
                       "@_get_daily_samples_size_websites_13, "
                       "@_get_daily_samples_size_websites_14, "
                       "@_get_daily_samples_size_websites_15, "
                       "@_get_daily_samples_size_websites_16, "
                       "@_get_daily_samples_size_websites_17, "
                       "@_get_daily_samples_size_websites_18, "
                       "@_get_daily_samples_size_websites_19, "
                       "@_get_daily_samples_size_websites_20, "
                       "@_get_daily_samples_size_websites_21, "
                       "@_get_daily_samples_size_websites_22, "
                       "@_get_daily_samples_size_websites_23, "
                       "@_get_daily_samples_size_websites_24, "
                       "@_get_daily_samples_size_websites_25 ")
        result_args_get_time = cursor.fetchone()

        result = []
        for i in range(len(result_args_get_time) - 2):
            result.append({
                'custom_data':
                result_args_get_time[i + 1],
                'label':
                get_timestamp_query(PERIOD.DAILY, i, result_args_get_time[-1])
            })

        return result
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


def resources_get_samples_size_weekly(mysql, resource_name):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        """
        Compatibility warning: PEP-249 specifies that any modified
        parameters must be returned. This is currently impossible
        as they are only available by storing them in a server
        variable and then retrieved by a query. Since stored
        procedures return zero or more result sets, there is no
        reliable way to get at OUT or INOUT parameters via callproc.
        The server variables are named @_procname_n, where procname
        is the parameter above and n is the position of the parameter
        (from zero). Once all result sets generated by the procedure
        have been fetched, you can issue a SELECT @_procname_0, ...
        query using .execute() to get any OUT or INOUT values.
        """
        args = [
            resource_name, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
        ]

        cursor.callproc('get_weekly_samples_size_websites', args)
        cursor.execute("SELECT "
                       "@_get_weekly_samples_size_websites_0, "
                       "@_get_weekly_samples_size_websites_1, "
                       "@_get_weekly_samples_size_websites_2, "
                       "@_get_weekly_samples_size_websites_3, "
                       "@_get_weekly_samples_size_websites_4, "
                       "@_get_weekly_samples_size_websites_5, "
                       "@_get_weekly_samples_size_websites_6, "
                       "@_get_weekly_samples_size_websites_7, "
                       "@_get_weekly_samples_size_websites_8, "
                       "@_get_weekly_samples_size_websites_9, "
                       "@_get_weekly_samples_size_websites_10, "
                       "@_get_weekly_samples_size_websites_11, "
                       "@_get_weekly_samples_size_websites_12, "
                       "@_get_weekly_samples_size_websites_13, "
                       "@_get_weekly_samples_size_websites_14, "
                       "@_get_weekly_samples_size_websites_15, "
                       "@_get_weekly_samples_size_websites_16, "
                       "@_get_weekly_samples_size_websites_17, "
                       "@_get_weekly_samples_size_websites_18, "
                       "@_get_weekly_samples_size_websites_19, "
                       "@_get_weekly_samples_size_websites_20, "
                       "@_get_weekly_samples_size_websites_21, "
                       "@_get_weekly_samples_size_websites_22, "
                       "@_get_weekly_samples_size_websites_23, "
                       "@_get_weekly_samples_size_websites_24, "
                       "@_get_weekly_samples_size_websites_25, "
                       "@_get_weekly_samples_size_websites_26, "
                       "@_get_weekly_samples_size_websites_27, "
                       "@_get_weekly_samples_size_websites_28, "
                       "@_get_weekly_samples_size_websites_29 ")
        result_args_get_time = cursor.fetchone()

        result = []
        for i in range(len(result_args_get_time) - 2):
            result.append({
                'custom_data':
                result_args_get_time[i + 1],
                'label':
                get_timestamp_query(PERIOD.WEEKLY, i, result_args_get_time[-1])
            })
        return result
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


def resources_get_samples_size_monthly(mysql, resource_name):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        """
        Compatibility warning: PEP-249 specifies that any modified
        parameters must be returned. This is currently impossible
        as they are only available by storing them in a server
        variable and then retrieved by a query. Since stored
        procedures return zero or more result sets, there is no
        reliable way to get at OUT or INOUT parameters via callproc.
        The server variables are named @_procname_n, where procname
        is the parameter above and n is the position of the parameter
        (from zero). Once all result sets generated by the procedure
        have been fetched, you can issue a SELECT @_procname_0, ...
        query using .execute() to get any OUT or INOUT values.
        """
        args = [
            resource_name, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
        ]

        cursor.callproc('get_monthly_samples_size_websites', args)
        cursor.execute("SELECT "
                       "@_get_monthly_samples_size_websites_0, "
                       "@_get_monthly_samples_size_websites_1, "
                       "@_get_monthly_samples_size_websites_2, "
                       "@_get_monthly_samples_size_websites_3, "
                       "@_get_monthly_samples_size_websites_4, "
                       "@_get_monthly_samples_size_websites_5, "
                       "@_get_monthly_samples_size_websites_6, "
                       "@_get_monthly_samples_size_websites_7, "
                       "@_get_monthly_samples_size_websites_8, "
                       "@_get_monthly_samples_size_websites_9, "
                       "@_get_monthly_samples_size_websites_10, "
                       "@_get_monthly_samples_size_websites_11, "
                       "@_get_monthly_samples_size_websites_12, "
                       "@_get_monthly_samples_size_websites_13, "
                       "@_get_monthly_samples_size_websites_14, "
                       "@_get_monthly_samples_size_websites_15, "
                       "@_get_monthly_samples_size_websites_16, "
                       "@_get_monthly_samples_size_websites_17, "
                       "@_get_monthly_samples_size_websites_18, "
                       "@_get_monthly_samples_size_websites_19, "
                       "@_get_monthly_samples_size_websites_20, "
                       "@_get_monthly_samples_size_websites_21, "
                       "@_get_monthly_samples_size_websites_22, "
                       "@_get_monthly_samples_size_websites_23, "
                       "@_get_monthly_samples_size_websites_24, "
                       "@_get_monthly_samples_size_websites_25, "
                       "@_get_monthly_samples_size_websites_26, "
                       "@_get_monthly_samples_size_websites_27, "
                       "@_get_monthly_samples_size_websites_28, "
                       "@_get_monthly_samples_size_websites_29, "
                       "@_get_monthly_samples_size_websites_30, "
                       "@_get_monthly_samples_size_websites_31, "
                       "@_get_monthly_samples_size_websites_32")
        result_args_get_time = cursor.fetchone()

        result = []
        for i in range(len(result_args_get_time) - 2):
            result.append({
                'custom_data':
                result_args_get_time[i + 1],
                'label':
                get_timestamp_query(PERIOD.MONTHLY, i,
                                    result_args_get_time[-1])
            })
        return result
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()
