# This program works out whether a number is even or odd

# Solution

print("Welcome!! Here, you'll know if a number is even or odd\n")

number = int(input("Enter the number here\n")) 

if number % 2 == 0:
    print(f"{number} is even")
    
else:
    print(f"{number} is odd")
