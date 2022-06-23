import sys
sys.stdin = open('input.txt')

N = int(input())
P = sorted(list(map(int, input().split())))
for i in range(1, N):
    P[i] = P[i-1] + P[i]
print(sum(P))