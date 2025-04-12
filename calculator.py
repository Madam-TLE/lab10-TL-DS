"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

def square_root(a):
    try:
        return math.sqrt(a)
    except ValueError as e:
        print(e)

def hypotenuse(a, b):
    try:
        math.hypot(a, b)
    except ValueError as e:
        print(e)

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