#mplementing the divide Function
def divid(a, b):
    if b == 0:
        raise ValueError("The divisor cannot be zero.")
    return a / b
#Handling the Exception
try:
    result = divid(10, 0)
except ValueError as e:
    print(e)
#What happens if you call divide(10, 2)?
try:
    result = divid(10, 2)
    print(result)
except ValueError as e:
    print(e)
#What happens if you change the exception message in the raise statement?
def division(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b

try:
    result = division(10, 0)
except ValueError as e:
    print(e)

"""
Try raising a different type of exception, such as TypeError. What changes do you need to make?
To raise a TypeError instead of a ValueError, you would change the exception type in the raise statement 
and handle it in the except block accordingly.
"""
def divide(a, b):
    if b == 0:
        raise TypeError("The divisor cannot be zero.")
    return a / b

try:
    result = divide(10, 0)
except TypeError as e:
    print(e)
