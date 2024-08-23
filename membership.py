
#Bitwise Operators
"""
Bitwise operators are used to perform operations on individual bits of numbers. These operators perform operations bit by bit.
Here are the main bitwise operators:
1.	AND (&)
2.	OR (|)
3.	NOT (~)
4.	XOR (^)
5.	Left Shift (<<)
6.	Right Shift (>>)
"""
#	1. AND (&): This operator compares each bit of two numbers and returns 1 if both bits are 1, otherwise it returns 0.
#example
a = 5       # In binary: 0101
b = 3       # In binary: 0011
result = a & b  # Result: 0001 (which is 1 in decimal)
print(result)   


# 2.OR (|): This operator compares each bit of two numbers and returns 1 if at least one of the bits is 1.

a = 5       # In binary: 0101
b = 3       # In binary: 0011
result = a | b  # Result: 0111 (which is 7 in decimal)
print(result)   


#3.NOT (~): This operator inverts all the bits of the number (0 becomes 1, and 1 becomes 0).  in Python, it also changes the sign of the number.
#example
a = 5       # In binary: 0101
result = ~a  # Result: 1010 (which is -6 in decimal)
print(result)   

#4. XOR (^): This operator compares each bit of two numbers and returns 1 if the bits are different, otherwise it returns 0.
#example 
a = 5       # In binary: 0101
b = 3       # In binary: 0011
result = a ^ b  # Result: 0110 (which is 6 in decimal)
print(result)   


#5.Left Shift (<<): This operator shifts the bits of the number to the left by the specified number of positions, filling the rightmost bits with 0s.
#example
a = 5       # In binary: 0101
result = a << 1  # Result: 1010 (which is 10 in decimal)
print(result)    


#6.Right Shift (>>): This operator shifts the bits of the number to the right by the specified number of positions, discarding the rightmost bits.
#example
a = 5       # In binary: 0101
result = a >> 1  # Result: 0010 (which is 2 in decimal)
print(result)    


#Membership Operators 
"""
Membership operators are used to check whether a value is a member of a sequence (such as a string, list or tuple).
There are two main membership operators:
1.	in
2.	not in
"""

#1.in: This operator returns True if the specified value is found in the sequence, otherwise it returns False.
#example
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)  
print("grape" in fruits)   


#2.not in: This operator returns True if the specified value is not found in the sequence, otherwise it returns False.
#example 
fruits = ["apple", "banana", "cherry"]
print("banana" not in fruits)  
print("grape" not in fruits)   
