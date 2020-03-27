# Helpers for rendering metrics


# Wrapper avoiding div by ZERO
def div_0(x, y):
    if not y:
        return 0
    if not x:
        return 0
    xx = float(x)
    yy = float(y)
    if yy == 0:
        return 2147483647
    return xx / yy


# Less than implementation with None < Anything
def lt_w_none(val1, val2):
    if val1 is None:
        return True
    if val2 is None:
        return True
    return val1 > val2


def get_percent_w_none(val1, val2):
    if val1 is None or val1 == 0:
        return 100
    if val2 is None or val2 == 0:
        return 0
    return round(abs(val2 - val1) / val1, 2)
