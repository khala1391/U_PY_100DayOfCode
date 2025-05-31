## way#1 end with close()
# file =  open("day24/my_file.txt")
# # file =  open("day24/weather_data.csv")
# contents = file.read()
# print(contents)
# file.close()


# https://www.w3schools.com/python/module_os.asp
import os
print(os.getcwd())

## open and read

# C:\Users\khala\OneDrive\MyDoc\Documents\000_DataScience\02_PY\U_PY_100DayOfCode
# with open("day01/my_file.txt") as file:
# with open(r"day01\my_file.txt") as file:

# C:\Users\khala\OneDrive\MyDoc\Documents\000_DataScience\02_PY
# with open("../my_file.txt") as file:            # 1-level up 

# C:\Users\khala\OneDrive\MyDoc\Documents\000_DataScience
# with open("../../my_file.txt") as file:       # 2-level up

# C:\Users\khala\OneDrive\MyDoc\Documents
# with open("../../../my_file.txt") as file:    # 3-level up  

# C:\Users\khala\OneDrive\MyDoc\
# with open("../../../../my_file.txt") as file:    # 4-level up  

# C:\Users\khala\OneDrive\
# with open("../../../../../my_file.txt") as file:    # 5-level up

# C:\Users\khala\Desktop  ==> use absolute path
# with open("desktop/../../../../my_file.txt") as file:    # not worked
# with open("c:/users/khala/desktop/my_file.txt") as file:    # 5-level up  diff folder


# with open("./weather_data.csv") as file:
#     contents = file.read()
#     print(contents)



# open and overwrite
with open("./my_file.txt", mode = "w") as file:
    file.write("new context overwrite in file")

# open and append
with open("./my_file.txt", mode = "a") as file:
    file.write("\nnew message add in file ")

