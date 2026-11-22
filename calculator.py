"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# first push! part 2!
import math

def add(a, b):
    return (a + b)

def subtract(a, b):
    return (a - b)

def multiply(a, b):
    return (a * b)

def divide(a, b):
    if a == 0:
        raise ZeroDivisionError

    else:
        return (b/a)

def logarithm(a, b):
    if b < 0:
        raise ValueError

    else:
        math.log(a, b)

def exponent(a, b):
    math.pow(a, b)







