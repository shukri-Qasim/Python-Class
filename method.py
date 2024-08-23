"""
Methods: in OOP a method is a function that is defined with in a class and describes the behavior or action that an object can perform.
methods define how an object interacts with it is self and other objects.
methods can be taken on from one object to another
Attributes: these are variables that belong to an object. they define the properties or charecteristics of the object for example name,age,size,etc.

"""
#example1
#methods contain the behavior of an object. they define what an object can do.
class Person: 
    def talk(self):
        print("this girl speaks politely")
person=Person()
person.talk() 

#example2
class Car:
    def start(self):
        print("the car has started")
my_car=Car()
my_car.start()

#example3  class with an attribute and a method
class Dog:
    def __init__(self,name): #initializes the object attribute which help us to add objects
        self.name=name
    def bark(self):
            print(f"{self.name} is barking")
my_dog=Dog("Buddy")
my_dog.bark()

#example4 class with multiple attributes
class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
    def description(self): #it help us to print out a statement 
        print(f"{self.title}is written by{self.author}")
my_book=Book("Atomic Habit","Ahmed")
my_book.description()

#Example5 : Modifying an attribute after creation
class Phone:
    def __init__(self,brand):
        self.brand=brand
    def call(self):
        print(f"Calling from {self.brand} phone")
my_phone=Phone("Apple")
my_phone.call()

my_phone.brand=("Samsung")
my_phone.call()