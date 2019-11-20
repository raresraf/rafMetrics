# Helpers for rendering metrics


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