import sys
sys.stdin = open('input.txt')
from itertools import permutations


N = int(input())
A = list(map(int, input().split()))
max = 0
per = list(permutations(A))

for p in per:
    total = 0
    for i in range(N-1):
        interval = abs(p[i]-p[i+1])
        total += interval
    if total > max:
        max = total

print(max)

