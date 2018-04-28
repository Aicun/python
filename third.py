S = "abcdefg"

a = 0
L = []
for s in S:
    a += ord(s)
    L.append(ord(s))

print(a)
print(L)

M = map(ord, S)

print(list(M))

# for i in range(50):
#    print('hello %d \a' % i)


D = {1: 'a', 3: 'b', 4: 's', 8: 'k', 2: 'u'}
print(sorted(D))
