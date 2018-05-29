def isPrime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while(i * i <= number):
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True


primes = [2]

i = 3
while True:
    if isPrime(i):
        primes.append(i)

    if len(primes) == 10001:
        print(primes[10000])
        break
    i += 2
