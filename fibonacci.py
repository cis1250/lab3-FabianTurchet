#!/usr/bin/env python3

# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.
sequence_number = 0

while sequence_number <= 0:
  sequence_number = int(input("Enter the number of terms you would like in the sequence: "))
  if sequence_number <= 0:
    print("Enter a positive integer: ")

a, b = 0, 1
for i in range(sequence_number):
  print(a, end= ' ')
  a, b = b, a + b
print()
 


# Validate that the input is a positive integer.
# Use a for loop to print the Fibonacci sequence up to that many terms.
