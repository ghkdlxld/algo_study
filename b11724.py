import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10**6)

def dfs(x):
    now = x
    for go in range(1, N+1):
        if link[now][go] == 1 and visited[now][go] == 0:
            print(go)
            visited[now][go] = 1
            visited[go][now] = 1
            if sum(link[go]) != sum(visited[go]):
                dfs(go)
            else:
                dfs(now)


N, M = map(int, input().split())
link = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    link[u][v] = 1
    link[v][u] = 1

cnt = 0
visited = [[0]*(N+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, N+1):
        if link[i][j] == 1 and visited[i][j] == 0:
            dfs(i)
            cnt += 1

print(cnt)
