import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input().strip())
arr = [list(map(int, input().strip())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

def bfs(x, y, cnt):
    visited[x][y] = cnt
    q = deque()
    q.append((x, y))

    while q:
        i, j = q.popleft()
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if 0<=ni<N and 0<=nj<N and arr[ni][nj] == 1 and visited[ni][nj] == 0:
                q.append((ni, nj))
                cnt += 1
                visited[ni][nj] = cnt


    return cnt


ans = 0
house = []
for a in range(N):
    for b in range(N):
        if visited[a][b] == 0 and arr[a][b] == 1:
            ans += 1
            house.append(bfs(a,b,1))

print(ans)
house = sorted(house)
for x in house:
    print(x)
