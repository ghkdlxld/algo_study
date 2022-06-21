import sys
sys.stdin = open('input.txt')
from itertools import combinations
import copy
from collections import deque
input = sys.stdin.readline

def bfs(wall_map):
    q = deque()
    q.extend(virus)


    di = [0, 0, -1, 1]
    dj = [1, -1, 0, 0]

    while q:
        start = q.popleft()

        for k in range(4):
            ni = start[0] + di[k]
            nj = start[1] + dj[k]

            if 0<=ni<N and 0<=nj<M and wall_map[ni][nj] == 0:
                q.append((ni, nj))
                wall_map[ni][nj] = 2


  
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
wall = []
virus = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            wall.append((i, j))
        if arr[i][j] == 2:
            virus.append((i, j))

group = combinations(wall, 3)
ans = 0
for g in group:
    cnt = 0
    wall_map = copy.deepcopy(arr)
    for i in range(3):
        wall_map[g[i][0]][g[i][1]] = 1
    bfs(wall_map)
    for i in range(N):
        cnt += wall_map[i].count(0)
    if cnt > ans:
        ans = cnt

print(ans)

