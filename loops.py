"""
A loop is an instruction that tells the computer to repeat a performance of a certain task .
it is purpose is to execute a block of code multiple times until a specified condition is met.
Types of loops 
For loop
While loop
Do-While loop
"""
#For loop
"""
A for loop iteratives over a sequance ( like a list,tuple,string or range ) and executes a blok of code for each element 
"""
#Example1  counting with a loop 
def my_count(): 
     for item in range(10): # a for initiates the loop then item is a variable that checks on each value in the sequance one at time. Range is a function that Generates a sequance of numbers  over which a loop iterates.  
        print(item)
my_count()

#example2 accessing list of  elements with a loop 
def list():
    lang=['python', 'javascript','C','ruby','swift'] 
    for langs in lang : #lang is list
        print(langs) #langs is a variable 
list()
      
#Example3 Using a for loop with a parameter 
def parameter(num):
    for number in range (num):
        print(number)
parameter(5)

#Example4 conditional statement inside a loop 
def my_lang():
    Shuu=['python', 'javascript','C','ruby','swift']
    for langs in Shuu:
        if langs == 'python':
            print('you are currently in Python class')
my_lang()

#Example5 finding even numbers with a loop 
def even(num1):
    for numbers in range (num1):
     if numbers %2 == 0:
        print(numbers)
even(10)

