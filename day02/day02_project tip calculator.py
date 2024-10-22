#If the bill was $150.00, split between 5 people, with 12% tip.
#Each person should pay (150.00 / 5) * 1.12 = 33.6
# #Round the result to 2 decimal places.
# print("Welcome to the tip calculator!")
# bill = float(input("What was the total bill? $"))
# tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
# people = int(input("How many people to split the bill?"))
#
# tip_as_percent = tip / 100
# total_tip_amount = bill * tip_as_percent
# total_bill = bill + total_tip_amount
# bill_per_person = total_bill / people
# final_amount = round(bill_per_person, 2)
#
#
# # FAQ: How to round to 2 decimal places?
#
# # Find the answer in the Q&A here: https://www.udemy.com/course/100-days-of-code/learn/lecture/17965132#questions/13315048
#
#
# print(f"Each person should pay: ${final_amount}")
#

#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

bill = input("bill?\n")
person = input("person?\n")
percent = input("percent?\n")

# type of input is alwasys'string'
bill_float = float(bill)
person_int = int(person)
percent_int = int(percent)

#ppp pay per person
ppp = bill_float*(1+percent_int/100)/person_int
ppp_r = round(ppp,2)
print(f"each person should pay {ppp_r}.")



