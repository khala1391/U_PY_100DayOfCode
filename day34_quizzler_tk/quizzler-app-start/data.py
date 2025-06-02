import requests
import json

parameters = {"amount":10,
              "type": "boolean",
              "category":18
              }
url = 'https://opentdb.com/api.php'


r = requests.get(url=url, params=parameters)
data = r.json()

# print(data['results'])
# print(json.dumps(data['results'], indent=4))

question_data = data['results']
