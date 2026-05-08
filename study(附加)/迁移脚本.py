import json
import os
old_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'text.txt')
print(old_path)
new_path = 'users.json'

data = {}
with open(old_path, 'r', encoding='utf-8') as f:
    for line in f:
        username, pwd, attempts = line.strip().split(',')
        data[username] = {
            'password': pwd,
            'attempts_left': int(attempts)
        }
print(data)
with open(new_path, 'w') as f:
    json.dump(data, f, indent=4)