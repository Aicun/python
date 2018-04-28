numbers = set()  # type: set

max1 = 999//3
max2 = 999//5

for i in range(1, max1+1):
    numbers.add(i * 3)

for j in range(1, max2+1):
    numbers.add(j * 5)

sum = 0
for x in numbers:
    sum += x

print(sum)


def getResult(n, m):
    count = m//n
    return n * count * (1 + count) / 2


sum3 = getResult(3, 999)
sum5 = getResult(5, 999)
sum15 = getResult(15, 999)
print(sum3 + sum5 - sum15)
