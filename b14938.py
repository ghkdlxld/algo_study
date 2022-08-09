import sys
from collections import deque
sys.stdin = open('input.txt')

n, m, r = map(int, input().split())
item = [0] + list(map(int, input().split()))
area = [[0]*(n+1) for _ in range(n+1)]
for _ in range(r):
    a, b, l = map(int, input().split())
    area[a][b] = l
    area[b][a] = l

ans = 0

def bfs(i):
    global ans
    q = deque()
    q.append((i, 0))
    visited[i] = 1
    tmp = item[i]

    while q:
        now, d = q.popleft()
        for k in range(1, n+1):
            if area[now][k] != 0 and d + area[now][k] <= m:
                visited[k] += 1
                if visited[k] == 1:
                    tmp += item[k]
                q.append((k, d + area[now][k]))

    if tmp > ans:
        ans = tmp


for x in range(1, n+1):
    visited = [0] * (n + 1)
    bfs(x)

print(ans)