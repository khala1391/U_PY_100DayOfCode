
# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆
# Small Pizza: $15
# Medium Pizza: $20
# Large Pizza: $25
# Pepperoni for Small Pizza: +$2 >> multiple if2
# Pepperoni for Medium or Large Pizza: +$3 >> elif
# Extra cheese for any size pizza: + $1  >> multiple if3
# Write your code below this line 👇

# aware of case-sensitive S<>s, M<>m, L<>l

bill = 0

# multiple if1
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

# multiple if2
if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

# multiple if3
if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")
