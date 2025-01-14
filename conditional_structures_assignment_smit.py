# -*- coding: utf-8 -*-
"""Conditional_Structures_Assignment_SMIT.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Svv_8_YK3dhSukwjfC04_KGxwkRm6VVj
"""

def check_even_or_odd():
    number = int(input("Enter a number: "))
    if number % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")

# Example usage
check_even_or_odd()

def check_voting_eligibility():
    age = int(input("Enter your age: "))
    if age >= 18:
        print("You are eligible to vote.")
    else:
        print("You are not eligible to vote yet.")

# Example usage
check_voting_eligibility()

def check_number_sign():
    number = float(input("Enter a number: "))
    if number > 0:
        print("Positive")
    elif number < 0:
        print("Negative")
    else:
        print("Zero")

# Example usage
check_number_sign()

def age_group():
    age = int(input("Enter your age: "))
    if 0 <= age <= 12:
        print("Child")
    elif 13 <= age <= 19:
        print("Teenager")
    elif 20 <= age <= 59:
        print("Adult")
    else:
        print("Senior Citizen")

# Example usage
age_group()

def check_even_or_odd():
    number = int(input("Enter a number: "))
    if number % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")

# Example usage
check_even_or_odd()

def day_of_week():
    day = int(input("Enter a number between 1 and 7: "))
    if day == 1:
        print("Sunday")
    elif day == 2:
        print("Monday")
    elif day == 3:
        print("Tuesday")
    elif day == 4:
        print("Wednesday")
    elif day == 5:
        print("Thursday")
    elif day == 6:
        print("Friday")
    elif day == 7:
        print("Saturday")
    else:
        print("Invalid input! Please enter a number between 1 and 7.")

# Example usage
day_of_week()

def calculate_bmi():
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))
    bmi = weight / (height * height)

    if bmi < 18.5:
        print("Underweight")
    elif 18.5 <= bmi < 24.9:
        print("Normal weight")
    elif 25 <= bmi < 29.9:
        print("Overweight")
    else:
        print("Obesity")

# Example usage
calculate_bmi()

def calculate_grade():
    marks1 = float(input("Enter marks for subject 1: "))
    marks2 = float(input("Enter marks for subject 2: "))
    marks3 = float(input("Enter marks for subject 3: "))

    average = (marks1 + marks2 + marks3) / 3

    if 90 <= average <= 100:
        print("Grade A")
    elif 80 <= average < 90:
        print("Grade B")
    elif 70 <= average < 80:
        print("Grade C")
    else:
        print("Grade below C")

# Example usage
calculate_grade()