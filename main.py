import numpy as np
import math

def entered_function(x):
    return (2 * x * math.exp(x**2))-5

def funk_diff_1(x):
    return ((4*x**2)+2)*math.exp(x**2)

def funk_diff_2(x):
    return ((12*x)+8*(x**3))*math.exp(x**2)

def funk_print_range(start = -5, end = 6, step = 1):
    for i in range(start, end):
        print("|f(" + str(i) + ")\t|" + str(entered_function(i)), end="|\n")
    x = start
    while x <= end:
        if np.sign(entered_function(x)) != np.sign(entered_function(x + step)):
            print("Інтервал, на якому функція міняє знак: [{}, {}]".format(x, x + step))
            return x, x + step
        x += step


def scan_for_zeroes(start, end, step):
    pass

if __name__ == "__main__":
    funk_print_range()