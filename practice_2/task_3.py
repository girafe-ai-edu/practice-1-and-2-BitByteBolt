# -*- coding: utf-8 -*-
"""
Write a program to calculate the body mass index (BMI) of a person. The user must enter their height and weight, 
after which you use one of the formulas below to determine the index.
BMI = weight/height**2 
"""


#code here

try:

    # Asking users to enter their weight in kilograms and converting input into float. 
    weight = float(input("Enter your weight in kilograms: "))

    # Asking users to enter their height in meters and converting input into float
    height = float(input("Enter your height in meters: "))

    BMI = weight/height**2

    print(f"Your Body Mass Index is : {BMI:.2f}")

except ValueError:
    print("Expecting float. Please enter correct values.")

