import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


def bfs(x):
    ans = -1
    q = deque([x])

    while q:
        now = q.popleft()
        ans += 1

        for i in network[now]:
            if visited[i] != 1:
                visited[i] = 1
                q.append(i)

    return ans

N = int(input())
L = int(input())
network = [[] for _ in range(N+1)]
visited = [0]*(N+1)
for _ in range(L):
    a, b = map(int, input().split())
    network[a].append(b)
    network[b].append(a)

visited[1] = 1
print(bfs(1)) 