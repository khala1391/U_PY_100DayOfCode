# with open("day25/weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)
#     print("-------------------")
#     data = [datum.strip() for datum in data]
#     print(data)

import csv

# with open("day25/weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     # for row in data:
#     for i, row in enumerate(data):
#         # if row[1] != "temp":
#         if i > 0:
#             temperature.append(int(row[1]))
#     print(temperature)
    
# ------------------------


import pandas as pd

data = pd.read_csv("day25/weather_data.csv")
print(data)

# print(data['temp'])
# # type(data)
# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data['temp'].to_list()
# print(temp_list)

# print(len(temp_list))

# data['temp'].mean()
# data['temp'].mean().round()

# data['temp'].max()
# data['condition']
# data.condition

# data[1:2]
# data[data.day == "Monday"]
# data[data.temp == data.temp.max()]
# data[data.temp == data.temp.min()]

# monday = data[data.day == "Monday"]
# monday.condition

# monday_temp = monday.temp[0]
# monday_temp_F = monday_temp * 9/5 +32
# monday_temp_F



# #create df from scratch
# data_dict = {
#     "student": ["Amy", "James", "Angela"],
#     "score": [76, 56, 65]
#     }

# data = pd.DataFrame(data_dict)
# data.to_csv("day25/new_data.csv")


# ---------------
import pandas as pd

data = pd.read_csv("day25/squirrel/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

data.columns

grey_squirrels_count = len(data[data['Primary Fur Color'] == "Gray"])
red_squirrels_count = len(data[data['Primary Fur Color'] == "Cinnamon"])
black_squirrels_count = len(data[data['Primary Fur Color'] == "Black"])

grey_squirrels_count
red_squirrels_count
black_squirrels_count

data_dict = {
    "Fur Color":  ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count,red_squirrels_count,black_squirrels_count]
}

df = pd.DataFrame(data_dict)
df.to_csv("day25/squirrel/squirrel_count_ojt.csv")