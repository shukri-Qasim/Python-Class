"""
in pytho 3 (input) is a function which is  used to capture  user input from the keyboard.
it always returns the input as string
"""
#example1

user_input=  input ("Enter any thing:")
print("You have entered:",user_input)

#example2
"""
Since input returns a string we need to convert the input the other datatypes(like integers or floats) as needed.
"""
age = input ("Enter your age : ")
print (" Your age as string :", age)

#example3
age_int= int(age)
print ("your age as integer: ",age_int)

#example4
name = input("Enter yout name: ")
print("Hello," + name +"!")



