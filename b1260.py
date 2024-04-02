import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline



def dfs(i):
    visited = [0]*(N+1)
    stack = [i]

    while stack:
        node = stack.pop()
        visited[node] = 1
        print(node, end=' ')

        for x in range(1, N+1):
            if link[node][x] == 1 and visited[x] != 1:
                stack.append(x)
                break


def bfs(i):
    visited = [0]*(N+1)
    q = deque([i])
    visited[i] = 1

    while q:
        node = q.popleft()
        print(node, end=' ')
        for x in range(1, N+1):
            if link[node][x] == 1 and visited[x] != 1:
                q.append(x)
                visited[x] = 1




N, M, V = map(int, input().split())
link = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    link[a][b] = 1
    link[b][a] = 1


dfs(V)
print()
bfs(V)