import time
from math import sqrt

# hello :bbbb
def solve(a, b, c): # args should not be 0
    delta = (b * b) - (4 * a * c)
    try:
        if delta == 0:
            return "S = {" + str(round(-b / (2 * a), 2)) + " }"

        if delta > 0:
            return "S = { " + str(round(((-b) - (-sqrt(delta))) / (2 * a), 2)) + " ; " + str(
                round(((-b) - (sqrt(delta))) / (2 * a), 2)) + " }"

        if delta < 0:
            return "S = { " + str(round((-b) / (2 * a), 2)) + str(round((-(sqrt(-delta))) / (2 * a), 2)) + "i ; " + str(
                round((-b) / (2 * a), 2)) + "+" + str(round((+(sqrt(-delta))) / (2 * a), 2)) + "i }"

    except ZeroDivisionError:
        return "Can't divide by 0...losar"
