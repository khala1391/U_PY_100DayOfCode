# 🚨 Don't change the code below 👇
height = input("enter your height in m: \n")
weight = input("enter your weight in kg: \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# convert input(always as 'str') to 'int' or 'float'
height_as_float = float(height)
weight_as_int = int(weight)

#int >> cut number regardless what it is
#round >> take value for consideration > roundup or down


# Using the exponent operator **
bmi = weight_as_int / height_as_float ** 2
# or using multiplication and PEMDAS
bmi = weight_as_int / (height_as_float * height_as_float)

bmi_as_int = round((bmi),2)

print(bmi_as_int)