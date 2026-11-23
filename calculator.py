"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.

https://github.com/jacooobbb12/lab10-JR-CC
Partner 1: Caleb Clements
Partner 2: Jacob Rosen
"""
# first push! part 3 !
import math

def square_root(a):
    if a < 0:
        raise ValueError

    else:
        return math.sqrt(a)

def hypotenuse(a,b):
    return math.hypot(a,b)

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
        return math.log(a, b)

def exponent(a, b):
    math.pow(a, b)







