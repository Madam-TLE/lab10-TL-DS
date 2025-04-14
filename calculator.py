# https://github.com/Madam-TLE/lab10-TL-DS.git
# Partner 1: Trish Le
# Partner 2: Diego Salazar

import math

def square_root(a):

    try:
        math.sqrt(a)
    except ValueError:
        raise ValueError
    return math.sqrt(a)

    if a <= 0:
        raise ValueError
    return math.sqrt(a)


def hypotenuse(a, b):
    try:
        math.hypot(a, b)

    except TypeError:
        raise TypeError
    return math.hypot(a, b)


    #if type(a) == str:
    #   raise TypeError
    #if type(b) == str:
    #    raise TypeError
    #return math.hypot(a, b)



def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    #try:
    #    a / b # raise ZeroDivisionError if a == 0
    #except ZeroDivisionError as e:
    #    print(e)
    #might have to raise ZeroDivisionError instead of try-excepting so self.assertRaises(ZeroDivisionError) works
    #in the test_divide_by_zero function
    if a == 0:
        raise ZeroDivisionError
    return b / a

def logarithm(a, b):
    #try:
    #    a.log(b)
    #except ValueError as e:
    #   print(e)
    # might have to raise ValueError instead of try-excepting so
    if b <= 1:
        raise ValueError
    return math.log(a,b)

def exp(a, b):
    a**b