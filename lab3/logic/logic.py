# Name:       Acacia Moran
# Course:     CPE 101
# Instructor: Nupur Garg
# Assignment: Lab 3
# Term:       Spring 2017

def is_even(number):
    x = number%2 == 0
    return x

def is_an_interval(n):
    x = ((n >= 2 and n < 9) or 
         (n > 47 and n < 92) or
    (n > 12 and n <= 19) or
    (n >= 101 and n <= 103))
    return x

