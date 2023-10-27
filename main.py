import json

with open('data.json') as file:
    data = json.load(file)

print(data['name'])
print(data['contacts']['email'])

data['is_admin'] = True

with open('result.json', 'w') as file:
    json.dump(data, file, indent=2)
