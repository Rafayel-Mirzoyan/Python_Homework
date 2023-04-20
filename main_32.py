import json

### 1 #write a python program to add into in JSON file about you

user  = input("Input about you: ")
with open("About_me.json", 'w') as file:
    json.dump(user, file)


### 2 #write a python program to get info in JSON file about you

with open("About_me.json", 'r') as file:
    result = json.load(file)
    print(result)

### 3 #write a python program to check if your json file have this info
search = input("Find: ")
with open("About_me.json", 'r') as file:
    result = json.load(file)
print(search in result)