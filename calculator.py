"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# https://github.com/Madam-TLE/lab10-TL-DS.git
# Partner 1: Trish Le
# Partner 2: Diego Salazar

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
    try:
        a / b # raise ZeroDivisionError if a == 0
    except ZeroDivisionError as e:
        print(e)

def logarithm(a, b):
    try:
        a.log(b)
    except ValueError as e:
        print(e)

def exp(a, b):
    a**b