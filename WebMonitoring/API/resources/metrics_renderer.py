from WebMonitoring.API.resources.numerical_helpers import lt_w_none, get_percent_w_none


def render_dict(
    result_args_get,
    result_args_old_get,
    list_sample,
    product_name,
    color,
    roundDecimal=2,
):

    return {
        "product": product_name,
        "total": {
            "monthly": round(result_args_get[3], roundDecimal),
            "weekly": round(result_args_get[2], roundDecimal),
            "daily": round(result_args_get[1], roundDecimal),
            "percent": {
                "value":
                get_percent_w_none(result_args_old_get[2], result_args_get[2]),
                "profit":
                lt_w_none(result_args_old_get[2], result_args_get[2]),
            },
        },
        "color": color,
        "lowest": {
            "monthly": {
                "value": round(result_args_get[6], roundDecimal),
                "profit": lt_w_none(result_args_old_get[6],
                                    result_args_get[6]),
            },
            "weekly": {
                "value": round(result_args_get[5], roundDecimal),
                "profit": lt_w_none(result_args_old_get[5],
                                    result_args_get[5]),
            },
            "daily": {
                "value": round(result_args_get[4], roundDecimal),
                "profit": lt_w_none(result_args_old_get[4],
                                    result_args_get[4]),
            },
        },
        "median": {
            "monthly": {
                "value": round(result_args_get[9], roundDecimal),
                "profit": lt_w_none(result_args_old_get[9],
                                    result_args_get[9]),
            },
            "weekly": {
                "value": round(result_args_get[8], roundDecimal),
                "profit": lt_w_none(result_args_old_get[8],
                                    result_args_get[8]),
            },
            "daily": {
                "value": round(result_args_get[7], roundDecimal),
                "profit": lt_w_none(result_args_old_get[7],
                                    result_args_get[7]),
            },
        },
        "highest": {
            "monthly": {
                "value": round(result_args_get[12], roundDecimal),
                "profit": lt_w_none(result_args_old_get[12],
                                    result_args_get[12]),
            },
            "weekly": {
                "value": round(result_args_get[11], roundDecimal),
                "profit": lt_w_none(result_args_old_get[11],
                                    result_args_get[11]),
            },
            "daily": {
                "value": round(result_args_get[10], roundDecimal),
                "profit": lt_w_none(result_args_old_get[10],
                                    result_args_get[10]),
            },
        },
        "samples": list_sample,
    }
