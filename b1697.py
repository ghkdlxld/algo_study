import sys
input = sys.stdin.readline
from collections import deque

def method(i, n):
    if i == 0:
        return n-1
    elif i == 1:
        return n+1
    else:
        return n*2

def bfs(n, k):
    q = deque([n])

    while q:
        now = q.popleft()
        for i in range(3):
            res = method(i, now)
            if 0 <= res < 100001 and road[res] == 987654321:
                road[res] = road[now] + 1
                q.append(res)

            if res == k:
                return



road = [987654321]*(100001)
N, K = map(int, input().split())
road[N] = 0
if N == K:
    print(0)
else:
    bfs(N, K)
    print(road[K])
