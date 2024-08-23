#Dynamic functions with parameters allow us to create functions that accept input values not as parameters when they are called 
#this parameters provide the function with the neccessary to perform  it is task making the function more versatile andn re-usable.
#example1
def add(num1,num2):      #inside the define function we have a parameters or arguments
    num3 = num1+num2
    print(num3)
add(1,3)    #these are values 

    #example2
def mod(num1,num2):
    num3 =num1%num2
    print(num3)
mod(5,2)
 #example3

def sub (num1,num2):
    num3 = num1-num2 
    print(num3)
sub(3,9)

#example4
def multi(num1,num2):
    num3=num1*num2
    print(num3)
multi(4,5)
