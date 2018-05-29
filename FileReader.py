def countLines(name):
    # file.seek(0)
    # return len(file.readlines())
    lines = 0
    for line in open(name):
        lines += 1
    return lines


def countChars(name):
    # file = open(name)
    # return len(file.read())
    chars = 0
    for line in open(name):
        chars += len(line)
    return chars


def test(name):
    # file = open(name)
    return countLines(name), countChars(name)


if __name__ == '__main__':
    print(test('FileReader.py'))
