"""
Constructors are special methods in python classes that are automatically called when are new instances or class is created.
they are used to initiallize the attributes of new objects .

KEY CONCEPTS
1._init_method():
this method is called Constructor.
it is used to initialize objects attributes when the object is instantiated.
this method takes at least one parameter:"self" which refers the current instance of the class.
2."self" parameter: is a reference of the instance of the class it self.
it allows access to classes attriutes and methods. while self is a conventional name it can technically be anything, but using self is a common practice.
3.Instantiation :
creating instance in a class is called Instantiation .
during Instantiation , values are passed to the _init_ method to initialize the object attributes .
4. 'pass' Statement: the "pass" statement is a place holder that does nothing.
it is used where code is syntatically required but not yet implemented .
"""
#example1 
class School:
     def __init__(self,name,location,teacher,student,motto):
        self.name=name
        self.location= location 
        self.teacher= teacher
        self.student= student
        self.motto= motto
     def register(self):
        print(f"{self.name} is fully registered")
school1=School("Alam","Hargeisa","Jackson",2000,"my countery")
school2=School("Noradin","jig-jiga yar","Mohamed",4000,"our countery")
school1.register()
school2.register()

#example2
class Countery:
    def __init__(self,name1,city,population):
        self.name1=name1
        self.city=city
        self.population=population
    def countery1(self):
        print(f"{self.city}in {self,name1}has {self.population}people")
Countery1= Countery("Somaliland","Hargeisa",1000)
countery1.countery1()

