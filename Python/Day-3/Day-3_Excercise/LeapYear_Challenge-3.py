# Challenge-3 Leap Year

#Write a program that works out whether a given year is a leap year. A normal year has 365 days, leap years have 366, with an extra day in February. The reason why we have leap years is really fascinating, this video does it more justice:

 #e.g. The year 2000:
 #2000 ÷ 4 = 500 (Leap)
 #2000 ÷ 100 = 20 (Not Leap)
 #2000 ÷ 400 = 5 (Leap!)
 #So the year 2000 is a leap year.
 #But the year 2100 is not a leap year because:
 #2100 ÷ 4 = 525 (Leap)
 #2100 ÷ 100 = 21 (Not Leap)
 #2100 ÷ 400 = 5.25 (Not Leap)
  
#Answer:
year = int(input("Which year do you want to check? "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not Leap Year")
    else:
        print("Leap Year")
else:
    print("Not Leap Year")