import sys
from itertools import combinations

while True:
    A = list(map(int, sys.stdin.readline().split()))
    if A == [0]:
        break
    else:
        k = A[0]
        S = A[1:]
        for x in list(combinations(S, 6)):
            for y in x:
                print(y, end=' ')
            print()
        print()