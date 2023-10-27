import requests

data = requests.get('https://pokeapi.co/api/v2/pokemon/pikachu')
if data.ok:
    pokemon = data.json()
    print(pokemon['name'])
    print(pokemon['height'])
    print(pokemon['weight'])
else:
    print('Something bad has happened')
