# agenda
# randomisation
# python list

# random is module for which we can call for
import random
random_int = random.randint(1,10)
print(random_int)
# random.randrange >> for ??

# test call module for another file
import day4_ex1HorT
print(day4_ex1HorT.vartest_module)

# https://www.askpython.com/python-modules/python-random-module-generate-random-numbers-sequences
print(random.random())
print(5*random.random())

#https://docs.python.org/3/tutorial/datastructures.html

# list.append(x)   >> add to the last
# list.extend(iterable)
# list.insert(i,x)
# list.remove(x)
# list.pop([i])
# list.clear()
# list.index(x,[start[,end]])
# list.count(x)
# list.sort()
# list.reverse()
# # list.copy()
#
# fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
# fcount1 = fruits.count('apple')
# fcount2 = fruits.count('tangerine')
# findex1 = fruits.index('banana')  #index start from 0
# findex2 = fruits.index('banana', 4)  # Find next banana starting at position 4
# # freverse = fruits.reverse()  # ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']
# # fruits.append('grape') # ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']
# # fruits.sort() #['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']
# # fruits.pop(2)  # delete data
#
# # print(fcount1)
# # print(findex2)
# # print(freverse) # >>> show 'none': not work because list name is still fruits
# print(fruits)

# stack = [3, 4, 5]
# # stack.append(6)
# # print(stack)
# print(fruits[0])  #orange
# print(fruits[1])  #apple
# print(fruits[-1]) #banana
# print(fruits[-3]) #kiwi
#
# fruits[0] = 'coconut'
# print(fruits)
# fruits.extend(["cat","dog"])
# print(fruits)
#
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

print(len(states_of_america))
# print(states_of_america)
#
#
# dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

word = "dog cat hen duck"
lsplt = word.split()
print(lsplt)

word = "d@g, c@t, h@n, d@ck"
lsplt2 = word.split(", ")
print(lsplt2)

stl = "yuttapong"
list_char = list(stl)
print(list_char)


a = ['one', 'eleven', 'twelve', 'five', 'six', 'ten']

print(a)

for i in range(3):
    print(random.choice(a))  # do not change list just randomize 5 times
print(a)  # list is the same

# dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]
# print(dirty_dozen)
# print(len(dirty_dozen))
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables =["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
dirty_dozen_new = [fruits, vegetables]
# print(dirty_dozen_new[1])
print(dirty_dozen_new)


gr1 = [["😀️","️😝"],"️😄"]
gr2 = [["😍️","😃️"],"😘"]
gr3 = [["🥰","🤪"],"😜️️"]
maps = [gr1, gr2, gr3]
print(f"{gr1}\n{gr2}\n{gr3}")

print(maps[1][0][0])  #😍️
print(maps[1][1])     #😘
print(maps[1][1][0])  #😘

# List of strings
l = ['sat', 'bat', 'cat', 'mat']

# https://www.geeksforgeeks.org/python-map-function/
# map() can listify the list of strings individually
test = list(map(list, l))
print(test)