# Less than implementation with None < Anything
def lt_w_none(val1, val2):
    if val1 == None:
        return True
    if val2 == None:
        return True
    return val1 > val2


def get_percent_w_none(val1, val2):
    if val1 == None:
        return 100
    if val2 == None:
        return 0
    return round(abs(val2 - val1) / val1, 2)


def render_dict(result_args_get, result_args_old_get, list_sample,
                product_name, color):

    return {
        "product": product_name,
        "total": {
            "monthly": round(result_args_get[3], 2),
            "weekly": round(result_args_get[2], 2),
            "daily": round(result_args_get[1], 2),
            "percent": {
                "value":
                get_percent_w_none(result_args_old_get[2], result_args_get[2]),
                "profit":
                lt_w_none(result_args_old_get[2], result_args_get[2])
            }
        },
        "color": color,
        "lowest": {
            "monthly": {
                "value": round(result_args_get[6], 2),
                "profit": lt_w_none(result_args_old_get[6], result_args_get[6])
            },
            "weekly": {
                "value": round(result_args_get[5], 2),
                "profit": lt_w_none(result_args_old_get[5], result_args_get[5])
            },
            "daily": {
                "value": round(result_args_get[4], 2),
                "profit": lt_w_none(result_args_old_get[4], result_args_get[4])
            }
        },
        "median": {
            "monthly": {
                "value": round(result_args_get[9], 2),
                "profit": lt_w_none(result_args_old_get[9], result_args_get[9])
            },
            "weekly": {
                "value": round(result_args_get[8], 2),
                "profit": lt_w_none(result_args_old_get[8], result_args_get[8])
            },
            "daily": {
                "value": round(result_args_get[7], 2),
                "profit": lt_w_none(result_args_old_get[7], result_args_get[7])
            }
        },
        "highest": {
            "monthly": {
                "value": round(result_args_get[12], 2),
                "profit": lt_w_none(result_args_old_get[12],
                                    result_args_get[12])
            },
            "weekly": {
                "value": round(result_args_get[11], 2),
                "profit": lt_w_none(result_args_old_get[11],
                                    result_args_get[11])
            },
            "daily": {
                "value": round(result_args_get[10], 2),
                "profit": lt_w_none(result_args_old_get[10],
                                    result_args_get[10])
            }
        },
        "samples": list_sample
    }
