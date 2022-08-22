import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

V = int(input())
graph = [[] for _ in range(V+1)]
for _ in range(V):
    arr = list(map(int, input().split()))
    for i in range(1, len(arr)-2, 2):
        graph[arr[0]].append([arr[i], arr[i+1]])

def dfs(x, cnt, ans):
    visited[x] = True
    for next, w in graph[x]:
        if not visited[next]:
            dfs(next, cnt + w, ans)

    if cnt > ans[1]:
        ans[0], ans[1] = x, cnt


n1 = [0,0]
visited = [False]*(V+1)
dfs(1, 0, n1)

n2 = [0, 0]
visited = [False]*(V+1)
dfs(n1[0], 0, n2)
print(n2[1])