# A program that calculates the BMI and interpretes the results

weight = input("Enter your weight in Kgs\n")
height = input("Enter your height in metres\n")

print(type(weight))
print(type(height))

weight = float(weight)
height = float(height)

BMI = (weight) / (height*height)

if BMI < 18.5:
    print(f"Your BMI is {BMI}, You are underweight")
elif BMI < 25:
    print(f"Your BMI is {BMI}, You have a normal weight")
elif BMI < 30:
    print(F"Your BMI is {BMI}, You are overweight")
elif BMI < 35:
    print(F"Your BMI is {BMI}, You are Obese")
else:
    print("You are clinically obese")