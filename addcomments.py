'''
Define a function named tests that takes two parameters, test1 and test2
'''

def tests(test1, test2):
    # Check if test1 is equal to test2
    if test1 == test2:
        # If they are equal, return test1 (could also return test2 as they are the same)
        return test1
    else:
        # If they are not equal, return test2
        return test2

# Allow  the user to enter marks for test one and convert the input to an integer using typecasting
test1 = int(input('Please enter Marks for test one: '))
# Allow the user to enter marks for test two and convert the input to an integer
test2 = int(input('Please enter Marks for test two: '))

'''
Define a function named courseWrk that takes one parameter, cswork (coursework marks)
'''
def courseWrk(cswork):
    # Call the tests function to determine the mark to use and assign it to testsMark
    testsMark = tests(test1, test2)
    # Calculate the average of the coursework mark and the test mark
    avgtestsCswork = (cswork + testsMark) / 2
    # Calculate the final coursework mark as 40% of the average mark
    fnltestsCswork = avgtestsCswork * (40 / 100)
    # Print the final coursework marks
    print('..............................')
    print('your final coursework marks is: ', fnltestsCswork)
    print('..............................')

# Allow the user to enter their coursework marks and convert the input to an integer
cswork = int(input('Please enter your course work Marks: '))
# Call the courseWrk function with the provided coursework marks
courseWrk(cswork)

#Description 
"""
This code calculates a student's final coursework marks based on their test scores and coursework marks.
The tests function compares two test marks and returns one of them based on specific criteria.
The courseWrk function computes the average of the coursework mark and the selected test mark, then calculates the final coursework mark as 40% of this average.
The user is allowed to input their test and coursework marks, and the final coursework mark is displayed.
"""