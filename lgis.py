from __future__ import print_function
import operator


def lgs(s, op=operator.lt):
    A = [0] * len(s)
    B = [None] * len(s)

    maxlength = 0
    for i in range(len(s)):
        f = ((A[j] + 1 if op(s[j], s[i]) else 1) for j in range(i + 1))
        B[i], A[i] = max(enumerate(f, 0), key=operator.itemgetter(1))
        if A[i] == 1:
            B[i] = -1
        if A[i] >= maxlength:
            pos, maxlength = i, A[i]

    ls = []
    while pos > -1:
        ls.append(s[pos])
        pos = B[pos]

    return ls[::-1]


def lgis(s):
    return lgs(s, op=operator.lt)


def lgds(s):
    return lgs(s, op=operator.gt)


if __name__ == "__main__":
    with open ('rosalind_lgis.txt') as dataset:
        x = int(dataset.readline().strip())
        y = [int(r) for r in dataset.readline().strip().split()]

    print(*lgis(y))
    print(*lgds(y))

