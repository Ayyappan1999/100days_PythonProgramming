# Challeneg-3

# Life in weeks

# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

# You have x days, y weeks, and z months left.

# Sample Input: 56 and Sample Output: You have 12410 days, 1768 weeks, and 408 months left.

# Answer:


age = input("What is your current age? ")
years = 90 - int(age)
weeks = round(years*52)
months = round(years*12)
days = round(years*365)

print(f" you have {days} days, {weeks} weeks, {months} months left.")
