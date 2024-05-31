# A program that works out whether a given year is a leap year. 
# A normal year has 365 days, leap years have 366 days with an extra day in February.
# NB:
# On every year that is divisble by 4
#  except every year that is evenly divisible by 100
#    unless the year that is also evenly divisible by 400  

# This means that if a year is evenly divisible by 4 and not evenly divisible by 100, it is a leap year 
# but if this year is evenly divisible by 4 and also divisible by 100, then it must also be evenly divisible by 400

# Solution

print("\n Here,you'll determine whether a year is leap or not!\n")

year = int(input("Enter the year year here\n"))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year")
        else:
            print(f"{year} is not a leap year")
    else:
        print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")              
    
        