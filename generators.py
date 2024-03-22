from typing import Any, Iterator
import requests


def s(a: int, b: int):
    yield a + b
    yield a * b


def repeater(value: Any):
    while True:
        yield value


def fibonacci(a: int = 0, b: int = 1) -> Iterator[int]:
    yield a
    yield b
    while True:
        a, b = b, a + b
        yield b


def get_people():
    url = 'https://swapi.dev/api/people'
    while url is not None:
        response = requests.get(url).json()
        for person in response['results']:
            yield person
        url = response['next']


print(*s(7, 6))

for x in s(9, 15):
    print(x)

for i, x in enumerate(fibonacci()):
    if i == 50:
        break
    print(x)

for person in filter(lambda p: p['height'] != 'unknown' and int(p['height']) >= 200, get_people()):
    print(person)
