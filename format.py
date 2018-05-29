def commas(n):
    digits = str(n)
    # assert(digits.isdigit())
    result = ""
    while digits:
        digits, last3 = digits[:-3], digits[-3:]
        result = (last3 + "," + result) if result else last3
    return result


def money(n, width=0):
    sign = "-" if n < 0 else ""
    n = abs(n)
    whole = commas(n)
    fract = ('%.2f' % n)[-2:]
    format = '%s%s.%s' % (sign, whole, fract)
    return '$%*s' % (width, format)


if __name__ == '__main__':
    def selftest():
        tests = 0, 1
        tests += 12, 123, 1234, 12345, 123456, 1234567
        tests += 2 ** 10, 2 ** 30
        for test in tests:
            print(commas(test))
        print('')

        tests = 0, 1, -1, 1.23, 1, 1.2, 3.14159
        tests += 12.23, 12.344, 12.345, 12.346
        tests += 2 ** 32, (2 ** 32 + .2345)
        tests += 1.2345, 1.2, 0.2345
        tests += -2.1243, -1.2, -0.2343
        tests += -(2 ** 10), -(2 ** 30)
        for test in tests:
            print('%s [%s]' % (money(test, 10), test))

    selftest()
