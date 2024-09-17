# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# -*- coding: utf-8 -*-

"""

Develop a program that asks the user for an integer 4-digit number 
and calculates the sum of its constituent digits. 
For example, if the user enters the number 3141, the program should 
output the following result:
3 + 1 + 4 + 1 = 9

"""


# Ask the user for a 4-digit integer
number = input("Please enter a 4-digit integer: ")


# Check if the input is a 4-digit integer
if len(number) == 4 and number.isdigit():
    
    
    # Calculate the sum of digits using list comprehension
    result = sum( int(digit) for digit in number )
    
    
    # Format and output the result
    calculation = " + ".join(number)
    
    
    print(f"{calculation} = {result}")
    
else:
    print("You must insert a 4-digit integer. Please double check your input.")


