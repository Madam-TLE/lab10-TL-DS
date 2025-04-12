"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

def add(a, b):
    a + b

def subtract(a, b):
    a - b

def multiply(a, b):
    a * b

def divide(a, b):
    try:
        a / b # raise ZeroDivisionError if a == 0
    except ZeroDivisionError as e:
        print(e)


def logarithm(a, b):
    try:
        a.log(b)
    except ValueError as e:
        print(e)

def exponent(a, b):
    a**b