import math


def f(x):
        y =( 7 * x ** 2 + 2 * x)
            return y


def g(x, y):
        z = (x ** 2 + y ** 2)
            return z


def hypotenuse(x, y):
        side_x = x
        side_y = y
        side_z= math.sqrt(side_x ** 2 + side_y ** 2)
        return side_z


def is_positive(x):
         return x > 0
