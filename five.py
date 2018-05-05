import math


def display(arg):
    print(arg)


display('abc')
display(123)
display([1, 2, 3])
display({'x': 1, 'y': 2})


def adder(first, second):
    return first + second


print(adder('abc', 'efg'))
print(adder([1, 2, 3], [4, 5, 6]))
print(adder(12.3, 12.3))


def adder2(*args):
    if isinstance(args[0], int):
        sum = 0
    else:
        sum = args[0][:0]
    for arg in args:
        sum += arg
    return sum


print(adder2(123, 456))


def adder3(*args):
    sum = args[0]
    for nx in args[1:]:
        sum += nx
    return sum


for func in (adder2, adder3):
    print(func(2, 3, 4))
    print(func('spam', 'eggs', 'toast'))
    print(func([1, 2], [3, 4], [5, 6]))


def adder4(**args):
    keys = list(args.keys())
    sum = args[keys[0]]
    for key in keys[1:]:
        sum += args[key]
    return sum


print(adder4(x=1, y=2, z=3))
print(adder4(x='abc', y='def', z='d'))


def copyDict(dict):
    res = {}
    for key in dict.keys():
        res[key] = dict[key]
    return res


print(copyDict({'x': 1, 'y': 3}))


def addDict(dict1, dict2):
    res = {}
    for key in dict1.keys():
        res[key] = dict1[key]
    for key in dict2.keys():
        res[key] = dict2[key]
    return res


print(addDict({'x': 1, 'y': 2}, {'x': 3, 'z': 4, 's': 5}))


def sf(args):
    res = []
    for x in args:
        res.append(math.sqrt(x))
    return res


def sf2(args):
    return list(map(math.sqrt(x), args))


def sf3(args):
    return [math.sqrt(x) for x in args]


def prime(x):
    if x <= 1:
        print(x, 'not prime')
    else:
        y = int(math.sqrt(x))
        while y > 1:
            print('y is', y)
            if x % y == 0:
                print(x, 'has factor', y)
                break
            y -= 1
        else:
            print(x, 'is prime')


prime(13)
prime(15)
