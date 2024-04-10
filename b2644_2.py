import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


n = int(input())
a, b = map(int, input().strip().split())
m = int(input().strip())
fam = [[] for _ in range(n+1)]
visited = [0]*(n+1)
visited[a] = 1

for _ in range(m):
    x, y = map(int, input().strip().split())
    fam[x].append(y)
    fam[y].append(x)

ans = -1
def dfs(i, cnt):
    global ans
    if i == b:
        ans = cnt
        return

    stack = []
    stack.append(i)

    while stack:
        now = stack.pop()
        for x in fam[now]:
            if visited[x] != 1:
                stack.append(x)
                visited[x] = 1
                dfs(x, cnt+1)
    return


dfs(a, 0)
print(ans)