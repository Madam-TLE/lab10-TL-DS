# https://github.com/Madam-TLE/lab10-TL-DS.git
# Partner 1: Trish Le
# Partner 2: Diego Salazar
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""


import math

def square_root(a):
    if a <= 0:
        raise ValueError
    return math.sqrt(a)

def hypotenuse(a, b):
    '''try:
        math.hypot(a, b)
    except TypeError as e:
        print(e)'''
    if type(a) == str:
        raise TypeError
    if type(b) == str:
        raise TypeError
    return math.hypot(a, b)


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
    if b == 0:
        raise ZeroDivisionError
    return a / b

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