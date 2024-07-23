#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator!")
#added a space before the final " in order for the cursor to come a space away from the prompt
bill=input("What was the total bill? $")
tip_perc=input("How much tip would you like to give? 10, 12, or 15? ")
numb_people=input("How many people to split the bill? ")
#bill will be inputed with a "$" as a string and so we need to convert this to a float and in order to do so we need to remove the "$". I can do that by subscripting the characters that start in position 1 -->[1:]
bill_per_per=round(float(bill)*(1+int(tip_perc)/100)/int(numb_people),2)
print(f"Each person should pay: ${bill_per_per}")
