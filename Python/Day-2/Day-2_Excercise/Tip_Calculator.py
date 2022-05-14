# Tip Calculator

print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tips = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))
average_tips = bill * tips /100
final_tips = bill + average_tips
total_amount = final_tips / people
print(f"Each Person should pay: {round(total_amount)}$ ")

