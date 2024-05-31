# An automatic pizza order program 

pizza_size = input("Which pizza size do you want? S, M or L\n")

bill = 0

if pizza_size == "S":
    bill += 15
elif pizza_size == "M":
    bill += 20
else:
    bill += 25

pepperoni = input("Do you want pepperoni? Y or N \n")

if pepperoni == "Y":
    if pizza_size == "s":
        bill += 2
    else:
        bill += 3
    
cheese = input("Do you want cheese? Y or N \n")

if cheese == "Y":
    bill += 1

print(f"Your total bill is: {bill}")
    

 

