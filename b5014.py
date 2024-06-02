import sys
from collections import deque
sys.stdin = open('input.txt')

F, S, G, U, D = map(int, input().split())
v = [10**6]*(F+1)

def bfs(x, y, f, b):
    q = deque()
    q.append(x)
    v[x] = 0

    while q:
        now = q.popleft()
        for k in (f, b):
            next = now+k
            if 0 < next <= F and v[next] > v[now]+1:
                q.append(next)
                v[next] = v[now]+1

bfs(S, G, U, -D)
print(v[G] if v[G] != 10**6 else 'use the stairs')