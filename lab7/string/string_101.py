from char import *

def str_rot_13(string):
    newstring = ''
    for i in string:
        newstring += char_rot_13(i)
    return newstring


def str_translate_101(string, a, b):
    newstring = ''
    for i in string:
        if i == a:
            newstring += b
        else:
            newstring += i
    return newstring
