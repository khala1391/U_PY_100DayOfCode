# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
# print(type(student_heights[0]))
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# print(student_heights)
# print(type(student_heights[0]))
# 🚨 Don't change the code above 👆

# Write your code below this row 👇


# local var in for loop is any word, can same name across loop
total_height = 0
for height in student_heights:
    total_height += height
print(f"total height = {total_height}")

number_of_students = 0
for student in student_heights:
    number_of_students += 1
print(f"number of students = {number_of_students}")

average_height = round(total_height / number_of_students)
print(average_height)