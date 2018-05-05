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


def getLargestPrime(number):

    primeFactor = 0

    i = 3

    while(i * i <= number):
        if number % i == 0:
            if(isPrime(i)):
                primeFactor = i
        i += 2

    return primeFactor


result = getLargestPrime(600851475143)
print(result)
