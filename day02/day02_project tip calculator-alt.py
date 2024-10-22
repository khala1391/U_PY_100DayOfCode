# At 13:20 you can see me using the round function to round the bill to 2 decimal places. But if the bill_per_person was a whole number ($12) or only had 1 decimal place ($12.4) then the round() function will not add a zero to format it with 2 decimal places.
#
# If you want it to look like this:
#
# $12 -> $12.00
#
# $12.4 -> $12.40
#
# Then you will need to Google for a custom solution.

# https://java2blog.com/format-a-float-to-two-decimal-places/
# https://docs.python.org/3/tutorial/floatingpoint.html


#If the bill was $150.00, split between 5 people, with 12% tip.
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Round the result to 2 decimal places.
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill?"))

#long form
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)

#If you want the final_amount to always have 2 decimal places.
#e.g. $12 becomes $12.00
#You can use this link to figure out how to do this:
#https://www.kite.com/python/answers/how-to-print-a-float-with-two-decimal-places-in-python
#This is how you can implement it:
final_amount = "{:.2f}".format(bill_per_person)

print(f"Each person should pay: ${final_amount}")