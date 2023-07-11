import json


with open("news.json", "r") as outfile:
            json_object=json.load(outfile)
for str in json_object:
    print(str)