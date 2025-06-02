print("-------------------------------------")

import random
# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for (key,value) in dict.itmes()}
# new_dict = {new_key:new_value for (key,value) in dict.itmes() if test}

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Elanor', 'Freddie']

student_scores = {name:random.randrange(50,100) for name in names}
print(student_scores)

# ---------------------------------------------------- 

passes_student = {k:v for k,v in student_scores.items() if v > 80 }
print(passes_student)

# ---------------------------------------------------- 

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

words = sentence.split()
# print(words)

result = {word:len(word) for word in words}


print(result)

# ---------------------------------------------------- 
weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}


weather_f = {key:value*9/5+32 for key,value in weather_c.items()}

print(weather_f)
# ---------------------------------------------------- 

student_dict = {
    "student": ['Angela', 'James', 'Lily'],
    "score": [56, 76, 98]
}


# loop through dictionary

## print keys line by line
for k,v in student_dict.items():
    print(k)
# print("-------------------------------------")


## print keys 1 line and value 1 line
for k,v in student_dict.items():
    print(v)
# print("-------------------------------------")


## print keys line by line
for k in student_dict.keys():
    print(k)
# print("-------------------------------------")


## print keys 1 line and value 1 line
for v in student_dict.values():
    print(v)
    

# ---------------------------------------------------- 
import pandas as pd


student_dict = {
    "student": ['Angela', 'James', 'Lily'],
    "score": [56, 76, 98]
}

student_df = pd.DataFrame(student_dict)
# print(student_df)

## loop through df

# for k,v in student_df.items():
#     print(k)
#     print(v)

# ---------------------------------------------------- 

## loop through row

for (idx,row) in student_df.iterrows():
    # print(idx)
    # print(row.student)
    # print(row.score)
    print(f"{row.student}:{row.score}")     # Angela:56
