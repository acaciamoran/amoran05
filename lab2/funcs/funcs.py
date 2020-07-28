import math


def f(x):
    y = 7 * x ** 2 + 2 * x
    return y

def g(x, y):
    z = x ** 2 + y ** 2
    return z


def hypotenuse(x, y):
    dist_x = x
    dist_y = y
    d = math.sqrt(dist_x ** 2 + dist_y ** 2)
    return d


def is_positive(x):
    return x > 0
