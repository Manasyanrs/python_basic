import requests
import json


url = requests.get("https://www.breakingbadapi.com/api/")
info_in_url = json.loads(url.text)
get_url = info_in_url.get("deaths")
new_get_url = requests.get(get_url)
result = json.loads(new_get_url.text)

death = 0
search_info = {}

for item in result:
    if item.get("number_of_deaths") > death:
        death = item.get("number_of_deaths")
        search_info.update(item)


with open("my_json.json", "w") as file:
    json.dump(search_info, file, indent=4)

with open("my_json.json", "r") as text:
    total_result = json.load(text)

print(total_result)

# зачет!
