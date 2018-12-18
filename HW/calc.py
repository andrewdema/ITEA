def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def divi(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        return e
def expon(a, b):
    return a ** b

