import sys
sys.stdin= open('input.txt')

N, K = map(int, input().split())
ppl = list(range(1, N+1))
ans = []
idx = -1
while ppl.count(0) != N:
    for _ in range(K):
        idx = (idx+1)%N
        while ppl[idx] == 0:
            idx = (idx+1)%N
    ans.append(ppl[idx])
    ppl[idx] = 0
print('<', end="")
print(*ans, sep=', ', end='>')