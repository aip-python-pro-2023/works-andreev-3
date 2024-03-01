def get_multiplier(a: int):
    def multiplier(b: int):
        return a * b

    return multiplier


def logger(func):
    def wrapper():
        print('Function is called')
        func()
    return wrapper


@logger
def greet():
    print('Hello')


# greet()
# # logger(greet)
# greet = logger(greet)
greet()

double = get_multiplier(2)
print(double(5), double(11))

triple = get_multiplier(3)
print(triple(5), triple(11))

data = [7, -9, 6, 4, 10, -6, 0]

print(data)
print(list(map(lambda x: x ** 3, data)))
print(list(filter(lambda x: x > 0, data)))
