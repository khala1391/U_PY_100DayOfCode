print("-------------------------------------")

numbers =[1,2,3]
new_list = []


## 1) for loop
for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)
# new_list
# print(new_list)

## 2) list comprehension
new_list2 = [n + 3 for n in numbers]
print(new_list2)

print("-------------------------------------")

name = "AngelaAngela"
letter_list = [i for i in name]
letter_list2 = list(name)

letter_set = {i for i in name}
letter_set2 = set(name)

name = "abcdefg"
letter_dictionary = {k:v for k,v in enumerate(name)}


print(letter_list)
print(letter_list2)
print(letter_list[1])

print(letter_set)
print(letter_set2)
# no indexing

print(letter_dictionary)
print(letter_dictionary[1])

# ---------------------------------------------------- 

double_list = [n*2 for n in range(1,6)]
print(double_list)

# ---------------------------------------------------- 

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Elanor', 'Freddie']
selected_list = [name for name in names if name[0] == "A"]
print(selected_list)

# ---------------------------------------------------- 
names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Elanor', 'Freddie']
selected_list = [name for name in names if 'a' in name]
# selected_list = [name for name in names if 'e' in name]
print(selected_list)

# ---------------------------------------------------- 
names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Elanor', 'Freddie']
selected_list = [name for name in names if len(name)>1  and name[1] == 'a']
print(selected_list)

# ---------------------------------------------------- 

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Elanor', 'Freddie']
index_dict = {name: [i for i, letter in enumerate(name) if letter == 'a'] for name in names if 'a' in name}
print(index_dict)

# ---------------------------------------------------- 
names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Elanor', 'Freddie']
selected_list = [name.capitalize() for name in names if len(name)>5]
print(selected_list)


# exercise
# ---------------------------------------------------- 

with open("day26/file1.txt") as f:
    contents_1 = f.readlines()
    contents_1 = [int(content.strip()) for content in contents_1]
    print(contents_1)



with open("day26/file2.txt") as f:
    contents_2 = f.readlines()
    contents_2 = [int(content.strip()) for content in contents_2]
    print(contents_2)


result = [num for num in contents_1 if num in contents_2]


print(result)