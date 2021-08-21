# Посмотреть документацию к API GitHub, разобраться как вывести список репозиториев для конкретного
# пользователя, сохранить JSON-вывод в файле *.json.
#

import json
import requests

response = requests.get("https://api.github.com/users/szgtshs/repos")

if response.ok:
    repo_list = response.json()
    for i in repo_list:
        print(i.get("name"))
with open("repo_data.json", "w") as r:
    json.dump(response.json(), r)
