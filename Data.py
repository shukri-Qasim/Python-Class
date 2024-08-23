#Data types are used define type of data , a variable or object can hold and how the computer system should interpret it's  value.
#categorization of values that are going to be stored a variable names prevents computer memory  wastage .
"""
examples of Different Datatypes 
Numeric Datatype 
String Datatype
Sequance or List Datatype
Mapping (Dict) Datatype
Booleans Datatypes 
Set datatype

Examples 
Numeric Datatype 
In numeric Datatypes we have : 
int (whole Number) 
Float (Decimal Number) 
Complex (1+2j)
"""
#Examples of Numeric Datatype

num1 = 1000
num2 = 10.3
num3 = 1+2j
num4 = "1000"
print(type(num1))
print(type(num2))
print(type(num3))
print(type(num4))

"""
String Datatype (str)
Any value in single or double quotes is a string .
"""
#Example
name = "Shukri"
print(type(name))

"""
Sequance/list 
this refers to a ordered list of elements or terms .
this elements can be numbers , charecters or any other datatype and they follow specific order.
"""
#example 
my_list = [0,2,4,6,]
print(type(my_list))
my_list2 = [0,2,4,6,"Shukri",0.5]
print(type(my_list2))

"""
Tuple 
it serves as an ordered collection of elements often used for grouping related data .
NOTE Tuples are immutable in python meaning their elements cannot be changed after creation  
"""
#example 
my_tuple = (0,2,4,6)
print(type(my_tuple))

"""
Mapping (dict)
 a dictionery is built in mapping type that consist of  a collection of key value pairs .
"""
#example 
my_dict = { 'Somaliland':'Hargeisa', 'Uganda':'Kampala', 'Tanzania':'Dodoma'}
print(type(my_dict))

"""
Booleans
Boolean datatypes are often denoted as true and false , they are designed to represent the two trues values of logic and boolean aljebra
"""
#example
num1 = True
num2 = False
print(type(num1))

"""
Set
set gives you unordered list of items
Note:it eliminate duplicate items .
"""

#example
my_set = {2,3,4,5,6}
my_set2 = {2,2,3,3,5,5,6,6,}
print(my_set)
print(my_set2)
print(my_dict)