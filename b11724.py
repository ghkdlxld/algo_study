import sys
sys.stdin = open('input.txt')

def dfs(x):
    stack = []
    stack.append(x)
    now = stack.pop()

    # 다 연결된 부분 갔다온 애를 check
    for go in range(1, N+1):
        if link[now][go] == 1 and visited[now][go] == 0 and (sum(link[go]) != sum(visited[go])):
            visited[now][go] = 1
            visited[go][now] = 1
            dfs(go)


N, M = map(int, input().split())
link = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    link[u][v] = 1
    link[v][u] = 1

cnt = 0
visited = [[0]*(N+1) for _ in range(N+1)]
while visited != link:
    for i in range(1, N+1):
        if sum(link[i]) != sum(visited[i]):
            dfs(i)
            cnt += 1
print(cnt)
