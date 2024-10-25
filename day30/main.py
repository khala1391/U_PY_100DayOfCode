## FileNotFoundError
# with open("not_existing_file.txt", mode='r', encoding ='utf-8') as f:
#     data= f.read()

## KeyError
# a_dictionary = {'key':'value'}
# print(a_dictionary['not_existing_key'])

## IndexError
# list = ['a','b','c']
# print(list[3])

## TypeError
# text ='abc'
# print(text +2)

# ----------------------------------------------------


# while True:
#     try:
#         numerator = 10
#         denominator = int(input("Enter a non-zero denominator: "))
#         result = numerator / denominator
#         print("Result:", result)
#         break  # Exit the loop if successful
#     except ZeroDivisionError:
#         print("Error: Division by zero is not allowed. Try again.")
#     except ValueError:
#         print("Error: Please enter a valid integer. Try again.")
#     except Exception as e:
#         print(f"An unexpected error occurred: {e}. Try again.")


# ----------------------------------------------------
# try:
#     pass
# except Exception as e:
#     raise e
# else:
#     pass

# ----------------------------------------------------

## FULL SYNTAX

# try:  # something that might cause an exception
#     pass
# except Exception as e:  # do this if there was an exception
#     raise
# else:   # do this if therer were no exception
#     pass
# finally:   # do this no matter what happens
#     pass


# r - open a file in read mode
# w - opens or create a text file in write mode
# a - opens a file in append mode
# r+ - opens a file in both read and write mode
# a+ - opens a file in both read and write mode
# w+ - opens a file in both read and write mode

# keyword 'Github issue'
# TODO
# BUG
# HACK
# FIXME

# ----------------------------------------------------
# with open("day30/a_file.txt", mode='r', encoding ='utf-8') as f:
#     data= f.read()
#     print(data)


# ----------------------------------------------------

try:
    file = open("a_file.txt")  # no file at same location
except:  
    print("there was an error")

# ----------------------------------------------------

from datetime import datetime
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
try:
    file = open("day30/a_file.txt")
except:  # too broad except
    file = open("day30/new_file.txt", "a")
    file.write(f"something new: write at {current_time}\n")
    file.close()            # required for case not in 'with' code block

# ----------------------------------------------------

from datetime import datetime
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

try:
    file = open("day30/dict_file.txt","a")  # pass
    a_dict = {'key':'value'}   # pass
    print(a_dict['non_existing_key'])  # KeyError
except KeyError as msg:
    log_file = open("day30/log_file.txt", "a")
    log_file.write(f"not found key {msg}: log at {current_time}\n")
    log_file.close()
    print(f"not found that key {msg}")
else:
    file.write("")
finally:
    file.close()

# ----------------------------------------------------

from datetime import datetime
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

try:
    file = open("day30/dict_file.txt","r")  # pass
    a_dict = {'key':'value'}   # pass
    print(a_dict['key'])  # pass
except KeyError as msg:
    log_file = open("day30/log_file.txt", "a")
    log_file.write(f"not found key {msg}: log at {current_time}\n")
    log_file.close()
    print(f"not found that key {msg}")
else:
    print("done")
finally:
    file.close()

# ----------------------------------------------------

while True:
    try:
        height = float(input("Height(m): "))
        weight = int(input("Weight(kg): "))
        
        if height >3:
            raise ValueError("Height is greater than 3, probably wrong unit")
        bmi = weight/height ** 2
        print(bmi)
        
        response = input(f"continue[y] or not[n]?: ")
        if response == 'n':
            break
        
    except ValueError as e:
        # Distinguish between the error types
        if "could not convert" in str(e):
            print("Please enter numeric values for height and weight.")
        else:
            print(e)

# ----------------------------------------------------

fruits = ["Apple", "Pear", "Orange"]

# Catch the exception and ensure the code runs without crashing.
def make_pie(index):
    try:
        fruit = fruits[index]
        print(fruit + " pie")
    except IndexError:
        print("Fruit pie")  # Fallback if the index is out of bounds

make_pie(3)


# ----------------------------------------------------

facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]


def count_likes(posts):

    total_likes = 0
    for post in posts:
        try:
            total_likes += post['Likes']
        except KeyError:
            total_likes += 0
    else:
        return total_likes


count_likes(facebook_posts)