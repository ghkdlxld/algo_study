import sys
from collections import deque


def bfs(i):
    q = deque()
    q.append(i)
    visited[i] = 1

    while q:
        now = q.popleft()
        for x in link[now]:
            if visited[x] == 0:
                q.append(x)
                visited[x] = 1


N, M = map(int, sys.stdin.readline().split())
link = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    link[u].append(v)
    link[v].append(u)

visited = [0] * (N + 1)
cnt = 0
for i in range(1, N + 1):
    if visited[i] == 0:
        bfs(i)
        cnt += 1

print(cnt)