"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

# First example
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ValueError("Cannot divide by 0.")
    return b / a

def log(a, b):
    if b <= 0:
        raise ValueError("Argument must be positive.")
    if a <= 0 or a == 1:
        raise ValueError("Base must be positive and not equal to 1.")
    return math.log(b, a)

def exp(a, b):
    return math.pow(a, b)



