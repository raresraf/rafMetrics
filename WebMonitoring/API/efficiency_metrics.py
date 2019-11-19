import pymysql


def div_0(x, y):
    if not y:
        return 0
    if not x:
        return 0
    xx = float(x)
    yy = float(y)
    if yy == 0:
        return 987654321
    return xx / yy


def get_results_resource_get_efficiency(result_args_get_time,
                                        result_args_old_get_time,
                                        list_sample_time, result_args_get_size,
                                        result_args_old_get_size,
                                        list_sample_size):
    result_args_get_efficiency = []
    result_args_old_get_efficiency = []

    for i in range(len(result_args_get_time)):
        result_args_get_efficiency.append(
            div_0(result_args_get_size[i], result_args_get_time[i]))
    for i in range(len(result_args_old_get_time)):
        result_args_old_get_efficiency.append(
            div_0(result_args_old_get_size[i], result_args_old_get_time[i]))
    list_sample_efficiency = []
    for i in range(len(list_sample_time)):
        list_sample_efficiency.append(
            div_0(list_sample_size[i], list_sample_time[i]))

    return (result_args_get_efficiency, result_args_old_get_efficiency,
            list_sample_efficiency)
