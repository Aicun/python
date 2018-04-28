def maker(N):

    def action(X):
        print(N ** X)
    return action


f = maker(5)
f(4)


def sum(L):
    # return L[0] if len(L) == 1 else L[0] + sum(L[1:])

    f, *r = L
    return f if not r else f + sum(r)


result = sum([1, 2, 3, 4, 5])
print(result)


def sumtree(L):
    total = 0
    for x in L:
        if not isinstance(x, list):
            total += x
        else:
            total += sumtree(x)
    return total


r = sumtree([1, [2, [3, 4], 5], 6, [7, 8]])
print(r)


def echo(text):
    print(text)


def indirect(func, arg):
    func(arg)


indirect(echo, "hello world")


def greet():
    first = "Hello"
    action = (lambda s: first + ' ' + s)
    return action


act = greet()
print(act('sir'))

L = [lambda x: x ** 2, lambda x: x ** 3, lambda x: x ** 4]

for f in L:
    print(f(2))

print(L[0](3))


action = (lambda x: (lambda y: x + y))

print(action(5)(5))
