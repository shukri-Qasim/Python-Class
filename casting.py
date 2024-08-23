"""
Type casting is a process of converting a value from one datatype to another.
Common type casting functions include 
int() this converts the value to an integer 
float() this converts the value to a float
str() this converts the value into a string 
list() this converts a value to a list
tupple() this converts a value to atuple 
"""
#example1
num_str = "123"
num_int = int(num_str)
print(num_int)

#example2
num_str="123.5"
num_float=float(num_str)
print(num_float)

#example3
num = 123
num_str2=str(num)
print(num_str2)

#example4
list=[1,2,3,4]
tuple=tuple(list)
print(tuple)

"""
Remember that input() in python 3 returns a string 
convert when neccesssary : use typecasting to convert the input of the required datatype before performing operations .
"""
#exercise
"""
calculate the area of rectangle based on user input 
"""
