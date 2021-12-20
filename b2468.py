import sys
sys.stdin = open('input.txt')
from collections import deque

def bfs(rain, visited, i, j):
    global safe, ans
    q = deque()
    q.append((i, j))
    visited[i][j] = 1

    while q:
        di = [0, 0, 1, -1]
        dj = [1, -1, 0, 0]
        now_i, now_j = q.popleft()
        for k in range(4):
            ni = now_i + di[k]
            nj = now_j + dj[k]
            if (0 <= ni < N) and (0 <= nj < N) and (visited[ni][nj] == 0) and (area[ni][nj] > rain):
                q.append((ni, nj))
                visited[ni][nj] = 1




N = int(input())
area = [list(map(int, input().split())) for _ in range(N)]
big = 0
for i in range(N):
    if max(area[i]) > big:
        big = max(area[i])
ans = 0
for rain in range(big):
    safe = 0

    visited = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0 and area[i][j] > rain:
                bfs(rain, visited, i, j)
                safe += 1

    if safe > ans:
        ans = safe

print(ans)