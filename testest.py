import json
import os

with open("config.json", "r") as f:
    data = json.load(f)
    print(os.getcwd())
    pw = os.getcwd()
    pw = "Eric.Dotson"
    pw.split("\\")
    # print(pw[2])
    pw = pw.split('.')
    print(pw)

# for name in data["users"]:
#     print(data["users"][0]["name"])
#     print(pw[2])
#     if pw[2] == data["users"][0]["name"]:
#         port = data["users"][0]["port"]
#         name = data["users"][0]["name"]

# name.split(".")
# print(name)
