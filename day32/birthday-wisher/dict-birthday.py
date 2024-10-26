from datetime import datetime
import pandas as pd
import random
import pprint
import json


today = datetime.now()
today_tuple = (today.month, today.day)

data = pd.read_csv("day32/birthday-wisher/birthdays.csv")
birthday_json = data.set_index("name").to_json(orient="index", indent=4)

with open("day32/birthday-wisher/birthdays.json", "w") as f:
    f.write(birthday_json)

# read JSON file
with open("day32/birthday-wisher/birthdays.json", "r") as f:
    birthday_dict = json.load(f)


# output for display
print(birthday_dict)  # poor format
print('-------------------------------------')
pprint.pprint(birthday_dict)  # print dict with pretty format
print('-------------------------------------')
print(json.dumps(birthday_dict, indent=4))  #convert dict to json



