"""
Lists are mutable data structures that can store multiple values
values in a list are accessed using indices starting from 0
Negative indices can be used to access values from the end of the list for example -1 from the last item 
"""
#example 
my_list = [0,1,2,3,4,5,6,7,8,9]
print(my_list[5])
print(my_list[2])
print(my_list[-1])

#example2
num1=[100,[200]]
print(num1[0])
print(num1[-2])
print(num1[1][0])
print(num1[-1]) #this give us position not the vslue 
print(num1[-1][-1]) #this give us value

"""
nonlisted  lists are simple lists that contain asereis of elements  which can be any data type (integer, string, float).
nested lists contain other lists in their elements
"""
#Tuples 
"""
 A tuple is a immutableb ie in tuples we ca access values but we can't add or remove anything 
 we access values the same way we access values in a list  
"""
#example
my_tuple=(10,20,30,40,50)
print(my_tuple[2])

#How to add , remove ,delete items in a list 

my_list2=[0,2,4,6,8]
my_list2.append(9) #this helps us to add values in a list 
print(my_list2)
my_list2.pop()  #this deletes a value (begining with the last value in the list)
print(my_list2)
my_list2.remove(0)  #this removes a specific  item from the list
print(my_list2)

fruits=["bananas","apples","mangoes"]
fruits.append("Lemon")
print(fruits)


#Dictioneries 
"""
it is identified by braces {} 
we can add or remove anything 
to see indices or keys we use  .keys()
to see values we use .values()
"""
#example 
my_dict={'Somaliland' :'Hargeisa','Uganda':'Kampala','Tanzania':'Dadama'}
print(my_dict.keys())
print(my_dict.values())

my_dict._delitem_('somaliland')
print(my_dict               )
