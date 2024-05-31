# This program  tests for compatibility between two people.

# Solution

name1 = input("Enter the first person's name:\n")
name2 = input("Enter the other person's name:\n")

# changing to lower case
lower_case_name1 = name1.lower()
lower_case_name2 = name2.lower()

# You can combine both names to make one string then continue as a single string

#Getting the number of times the letters in the name TRUE and LOVE occur in these names
# Name 1
name1_T = lower_case_name1.count("t")
name1_R = lower_case_name1.count("r")
name1_U = lower_case_name1.count("u")
name1_E = lower_case_name1.count("e")

name1_L = lower_case_name1.count("l")
name1_O = lower_case_name1.count("o")
name1_V = lower_case_name1.count("v")
name1_e = lower_case_name1.count("e")

#Name 2
name2_T = lower_case_name2.count("t")
name2_R = lower_case_name2.count("r")
name2_U = lower_case_name2.count("u")
name2_E = lower_case_name2.count("e")

name2_L = lower_case_name2.count("l")
name2_O = lower_case_name2.count("o")
name2_V = lower_case_name2.count("v")
name2_e = lower_case_name2.count("e")

# Totals of each letter in TRUE and LOVE
Total_T = name1_T + name2_T
Total_R = name1_R + name2_R
Total_U = name1_U + name2_U
Total_E = name1_E + name2_E

Total_L = name1_L + name2_L
Total_O = name1_O + name2_O
Total_V = name1_V + name2_V
Total_e = name1_e + name2_e

# Calculating the total for both
Total_for_True = str(Total_T + Total_R + Total_U + Total_E)
Total_for_Love = str(Total_L + Total_O + Total_V + Total_e)

# Making a 2 digit number
score = Total_for_True + Total_for_Love

score = int(score)

if (score<10) or (score>90):
    print(f"Your Score is {score}, you go together like coke and mentos")

elif (score >= 40) and (score <= 50):
    print(f"Your score is {score}, you are alright together")
    
else:
    print(f"Your score is {score}")
