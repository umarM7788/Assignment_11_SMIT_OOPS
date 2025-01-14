# -*- coding: utf-8 -*-
"""Assignment_02_SMIT.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1IiQy6lLm4YCqnQY_7R395FNwBvYwgsXV
"""

def area_of_rectangle():
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = length * width
    print(f"The area of the rectangle is: {area}")

# Example usage
area_of_rectangle()

import math

def circumference_of_circle():
    radius = float(input("Enter the radius of the circle: "))
    circumference = 2 * math.pi * radius
    print(f"The circumference of the circle is: {circumference}")

# Example usage
circumference_of_circle()

def simple_interest():
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the rate of interest: "))
    time = float(input("Enter the time in years: "))
    interest = principal * rate * time
    print(f"The simple interest is: {interest}")

# Example usage
simple_interest()

def speed_of_object():
    distance = float(input("Enter the distance covered (in meters): "))
    time = float(input("Enter the time taken (in seconds): "))
    speed = distance / time
    print(f"The speed of the object is: {speed} meters per second")

# Example usage
speed_of_object()

def force_calculation():
    mass = float(input("Enter the mass of the object (in kilograms): "))
    acceleration = float(input("Enter the acceleration (in meters per second squared): "))
    force = mass * acceleration
    print(f"The force on the object is: {force} Newtons")

# Example usage
force_calculation()

def perimeter_of_triangle():
    a = float(input("Enter the length of the first side: "))
    b = float(input("Enter the length of the second side: "))
    c = float(input("Enter the length of the third side: "))
    perimeter = a + b + c
    print(f"The perimeter of the triangle is: {perimeter}")

# Example usage
perimeter_of_triangle()

def compound_interest():
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the annual interest rate (in decimal): "))
    n = int(input("Enter the number of times interest is compounded per year: "))
    t = int(input("Enter the time in years: "))
    amount = principal * (1 + rate / n) ** (n * t)
    print(f"The total amount after {t} years is: {amount}")

# Example usage
compound_interest()
