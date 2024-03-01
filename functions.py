from typing import Union, List, Tuple, Dict

Number = Union[int, float]


def s(a: Number, b: Number, *args, **kwargs) -> Number:
    print(args)
    print(kwargs)
    return a + b + sum(args) + sum([kwargs[x] for x in kwargs])


res: Number = s(1, 2, 3.9, 4.77, 5, 6, 7, 8.0, i=9, j=10)
print(res)

greeting: str = 'Hello World!'
# greeting = 5

data: List[int] = [8, 7, 6, 5, 4, 3, 2, 1]
user: Tuple[str, str, int] = ('John', 'Smith', 33)

params: Dict[str, str] = {
    'sep': '\n',
    'end': '!'
}
print(*data, **params)
# print(8, 7, 6, 5, 4, 3, 2, 1, sep='\n', end='!')
