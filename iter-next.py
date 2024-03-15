from iterators import Repeater

data = Repeater(5)

iterator = iter(data)
print(iterator)

while True:
    try:
        item = next(iterator)
    except StopIteration:
        break

    print(item)

# for item in data:
#     print(item)
