def check_square():
        # Taking input from the user
        number = int(input("Please enter an integer: "))
        
        # Calculating the square of the number
        square = number ** 2
        
        # Determining if the square is even or odd and printing the appropriate message
        if square % 2 == 0:
            print(f"The square of {number} is {square}, which is even.")
        else:
            print(f"The square of {number} is {square}, which is odd.")
    
# Call the function
check_square()
