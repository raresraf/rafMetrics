from WebMonitoring.API.resources.last_seven_entries_metrics import (
    get_last_seven_entries_time, )


def get_results_resource_get_time(mysql, resource_name):
    result_args_get_time = []
    result_args_old_get_time = []
    list_sample = []

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
        args = [resource_name, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        cursor.callproc("resource_get_time", args)
        cursor.execute("SELECT @_resource_get_time_0, "
                       "@_resource_get_time_1, "
                       "@_resource_get_time_2, "
                       "@_resource_get_time_3, "
                       "@_resource_get_time_4, "
                       "@_resource_get_time_5, "
                       "@_resource_get_time_6, "
                       "@_resource_get_time_7, "
                       "@_resource_get_time_8, "
                       "@_resource_get_time_9, "
                       "@_resource_get_time_10, "
                       "@_resource_get_time_11, "
                       "@_resource_get_time_12 ")
        result_args_get_time = cursor.fetchone()

        cursor.callproc("resource_get_old_time", args)
        cursor.execute("SELECT @_resource_get_old_time_0, "
                       "@_resource_get_old_time_1, "
                       "@_resource_get_old_time_2, "
                       "@_resource_get_old_time_3, "
                       "@_resource_get_old_time_4, "
                       "@_resource_get_old_time_5, "
                       "@_resource_get_old_time_6, "
                       "@_resource_get_old_time_7, "
                       "@_resource_get_old_time_8, "
                       "@_resource_get_old_time_9, "
                       "@_resource_get_old_time_10, "
                       "@_resource_get_old_time_11, "
                       "@_resource_get_old_time_12 ")
        result_args_old_get_time = cursor.fetchone()

        list_sample = []
        samples = get_last_seven_entries_time(mysql, resource_name)
        for sample in samples:
            list_sample.append(int(1000 * sample["ResponseTime"] + 1))
    except Exception as e:
        print(e)
    finally:
        try:
            cursor.close()
            conn.close()
        except NameError:
            return (None, None, None)
        return (result_args_get_time, result_args_old_get_time, list_sample)
