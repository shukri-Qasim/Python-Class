"""
Inheritence is a fundamental concept in object  oriented programming that allows(child class) to inherit attributes and the methods from another class.
This helps in using code and establishing in natural hierarchy between classes.
Class parent :
    Parent class code 
Class child(Parent):
    Child class code

"""
#Sinle Inheritence 
"""
Single inheritence occurs  when the child class inherits from one one parent class. this is the simplest form of inheritence. 
"""
#SYNTAX
class Parent():
    def parent_method(self):
        print("this is a method of a parent class")
class Child(Parent):
    def child_method(self):
        print("this is a method ofa child class")
child=Child()
child.parent_method()
child.child_method()

#Example1
class Vehicle(): #this is a parent class

    def __init__(self,make,model):#constructor to give us attributes to be used in our objects
      self.make=make #creating attributes we shall assign values later 
      self.model=model
    def display_info(self):#this is a parent class method
     print(f"make:{self.make},model:{self.model}")

class Car(Vehicle): #this is a child class 
    def display_type(self):#this is a child class  method 
        print(f"{self.make}{self.model} is a car.")
my_car=Car("Vitz","Noah") #we are creating an instances of a car 
my_car.display_info() #using methos form the parent class
my_car.display_type() #using methos form the child class
