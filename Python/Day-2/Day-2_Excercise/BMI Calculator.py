# Day2_Challenge2

# BMI Calculator

# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.

# Sample Input: weight=80, height = 1.75

height = input("Enter your height in m:  ")
weight = input("Enter your weight in kg: ")
weight_in_integer = int(weight)
height_in_float = float(height)
bmi = weight_in_integer / (height_in_float * height_in_float)
print(int(bmi))