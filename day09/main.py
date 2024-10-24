colors ={
    "apple":"red",
    "pear":"green",
    "banana":"yellow"
}

# print(colors)
# print(colors['apple'])

# loop for key
for color in colors:
    print(color)

print('-------------------------------------')

# loop for value
for k in colors:
    print(colors[k])
    

# ---------------------------------------------------- 

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

# Dictionary comprehension with more than three conditions
student_grades = {
    k: ('Fail' if v < 70 else
        'Acceptable' if 71 <= v < 80 else
        'Exceeds Expectations' if 81 <= v < 90 else
        'Outstanding') 
    for k, v in student_scores.items()
}

print(student_grades)


# ---------------------------------------------------- 
# not dict comprehension

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

# Create an empty dictionary to collect the new values.
student_grades = {}
 
# Loop through each key in the student_scores dictionary
for student in student_scores:
 
# Get the value (student score) by using the key each time.
    score = student_scores[student]
 
# Check what grade the score would get, then add it to student_grades
    if score >= 91:
        student_grades[student] = 'Outstanding'
    elif score >= 81:
        student_grades[student] = 'Exceeds Expectations'
    elif score >= 71:
        student_grades[student] = 'Acceptable'
    else:
        student_grades[student] = 'Fail'

# ---------------------------------------------------- 

travel_log ={
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgard", "Berlin"]
}

print(travel_log['France'][1])

# ---------------------------------------------------- 


nested_list = ["a","b", ["c",["d","e"]]]

print(nested_list[0])
print(nested_list[2])
print(nested_list[2][0])
print(nested_list[2][1])
print(nested_list[2][1][1])

# ---------------------------------------------------- 


travel_log ={
    "France": {
        "num_times_visited" : 8,
        "cities_visited":["Paris", "Lille", "Dijon"]      
    },
    "Germany": ["Stuttgard", "Berlin"]
}

print(travel_log['France']['num_times_visited'])
print(travel_log['France']['cities_visited'])
print(travel_log['France']['cities_visited'][2])


# ---------------------------------------------------- 

dict = {
    "a": 1,
    "b": 2,
    "c": 3,
}

for key in dict:
    dict[key] +=1
    
print(dict)