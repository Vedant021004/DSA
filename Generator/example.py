def numbers():
    return [1, 2, 3, 4, 5]

result = numbers()

print(result)


def numbers():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

result = numbers()

print(result)


def numbers():
    for i in range(100):
        yield i

for num in numbers():
    print(num)


def numbers():
    yield 1
    yield 2
    yield 3

gen = numbers()

print(next(gen))
print(next(gen))
print(next(gen))    