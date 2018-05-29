count = 0
n = 1
while True:
    for x in range(1, n):
        if(n // x == 0):
            count += 1
    if(count > 500):
        break
    n += 1

print(count, n, sep=' ')
