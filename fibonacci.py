#!/usr/bin/env python3

# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.
# Validate that the input is a positive integer.
# Use a for loop to print the Fibonacci sequence up to that many terms.
input_user1 = 0
while (input_user1 <= 0):
    input_user = input("User input: ")
    input_user1 = int(input_user)
    forL = input_user1//2
    if(input_user1 > 0):
        x1 = 0
        x2 = 1
        x = forL
        if(input_user1%2 == 0):
            for x in range(forL):
                print(x1,x2,end = " ")
                x1+= x2
                x2+= x1
        else:
            for x in range(forL):
                print(x1,x2,end = " ")
                x1+= x2
                x2+= x1
            print(x1,end = " ")
    else:
        print("Please enter a positive integer.")
