# agenda
# for loops
# range
# code block

fruits = ["Apple", "Peach", "Pear"]
for item in fruits:
    print(item)
    print(item + " Pie")
print(fruits)

set = [1,2,3]
for item in set:
    print(item+1)
print(set)

# debug by pycharm
# https://www.youtube.com/watch?v=76Lu6CfMuGg

#for loop with list

for number in range(-1, 10):
    print(number)
print("xxxxxxxxxxxxxx")

for number in range(1, 11):
    print(number)
print("xxxxxxxxxxxxxx")

for number in range(2, 11,2):   #print 2 until less than 11 , by step as 2
    print(number)
print("xxxxxxxxxxxxxx")

total = 0
for number in range(1,101):
    total +=number
print(total)