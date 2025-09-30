#!/usr/bin/env python3

# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.

while True:
    sequence_number = input("Enter the number of terms you would like in the sequence: ")
    
    if sequence_number.isdigit():  
        sequence_number = int(sequence_number)
        if sequence_number > 0:
            break 
        else:
            print("Please enter a positive integer.")
    else:
        print("That's not a valid number. Try again.")

a, b = 0, 1
for i in range(sequence_number):
    print(a, end=' ')
    a, b = b, a + b
print()
 


# Validate that the input is a positive integer.
# Use a for loop to print the Fibonacci sequence up to that many terms.
