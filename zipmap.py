def myzip(*seqs):
    seqs = [list(S) for S in seqs]
    print(seqs)
    res = []
    while all(seqs):
        res.append(tuple(S.pop(0) for S in seqs))
    return res


print(myzip([1, 2, 3], [4, 5, 6, 7], [8, 9, 10]))


def myMap(*seqs, pad=None):
    seqs = [list(S) for S in seqs]
    print(seqs)
    res = []
    while any(seqs):
        res.append(tuple((S.pop(0) if S else pad) for S in seqs))
    return res


print(myMap('abc', 'xyzd'))
print(myMap('123', 'xyzabc', pad='HELLO'))


def myZipYield(*seqs):
    seqs = [list(S) for S in seqs]
    while all(seqs):
        yield tuple(S.pop(0) for S in seqs)


def myMapYield(*seqs, pad=None):
    seqs = [list(S) for S in seqs]
    while any(seqs):
        yield tuple((S.pop(0) if S else pad) for S in seqs)


def myMap2(*seqs):
    iters = list(map(iter, seqs))
    while iters:
        res = [next(i) for i in iters]
        yield tuple(res)


print(list(myMap2([1, 2, 3, 4])))
