from typing import Any


class Repeater:
    value: Any
    max_count: int
    count: int

    def __init__(self, value: Any, max_count: int) -> None:
        self.value = value
        self.max_count = max_count
        self.count = 0

    def __iter__(self):
        self.count = 0
        return self

    def __next__(self):
        self.count += 1
        if self.max_count < self.count:
            raise StopIteration
        return self.value


repeater = Repeater(5, 3)

for x in repeater:
    print(x)

print('---')

for x in repeater:
    print(x)
