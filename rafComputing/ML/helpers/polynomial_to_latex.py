def polynomial_to_LaTeX(p):
    """ Small function to print nicely the polynomial p as we write it in maths, in LaTeX code."""
    coefs = p.coef  # List of coefficient, sorted by increasing degrees
    res = ""  # The resulting string
    for i, a in enumerate(coefs):
        if int(a) == a:  # Remove the trailing .0
            a = int(a)
        if i == 0:  # First coefficient, no need for X
            if a > 0:
                res += "{a} + ".format(a=("%.2E" % a))
            elif a < 0:  # Negative a is printed like (a)
                res += "({a}) + ".format(a=("%.2E" % a))
            # a = 0 is not displayed
        elif i == 1:  # Second coefficient, only X and not X**i
            if a == 1:  # a = 1 does not need to be displayed
                res += "X + "
            elif a > 0:
                res += "{a} \;X + ".format(a=("%.2E" % a))
            elif a < 0:
                res += "({a}) \;X + ".format(a=("%.2E" % a))
        else:
            if a == 1:
                # A special care needs to be addressed to put the exponent in {..} in LaTeX
                res += "X^{i} + ".format(i="{%d}" % i)
            elif a > 0:
                res += "{a} \;X^{i} + ".format(a=("%.2E" % a), i="{%d}" % i)
            elif a < 0:
                res += "({a}) \;X^{i} + ".format(a=("%.2E" % a), i="{%d}" % i)
    return "$" + res[:-3] + "$" if res else ""
