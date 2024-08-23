"""
Exception handling in python  is a mechanism to handle runtime errors so that the normal flow of the application can be  maintained.
it helps in dealing with errors gracefully without crushing the program.
KEY CONCEPTS
1.Exception(Error): is an event which occurs  during the execution of a program that distrupts the normal flow of the program instruction.
2.Exception handling : the process of responding to the occurance of exception.

COMMON EXCEPTIONS
A.ZeroDivisionError: it is raised when Division by zero Error is attemped.
B.IndexError: it is raised when trying to access an element outside the list's elements.
C.KEY ERROR: it is raised when dictionery key is not found.
D.TYPE ERROR : it is raised when when an operation is applied to an objective inappropriate time.
E.Value Error :it is raised when a function receives an argument but inappropriate value.
"""
# BASIC SYNTAX 
# try:
#     #code that might  araise an exception 
# except SomeException:
    #code to handle exception 
# Example1 (handling division by zero)
try:
    result=10/0
except ZeroDivisionError:
    print("You can't divide by zero")
#Example2 handling multiple eceptions 
try:
    A= int(input("Enter a number: "))
    B=int(input("Enter another number: "))
    result=A/B
except ValueError:
    print("Invalid input please enter numbers only")
except ZeroDivisionError:
    print("You can't divide by zero")
else:
    print(result)