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
