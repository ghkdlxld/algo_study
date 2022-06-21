import sys
sys.stdin = open('input.txt')
from collections import deque

def bfs(i, j, cnt):
    global shark_size
    way = deque()
    way.append([i, j])

    # 상 좌 하 우
    di = [-1, 0, 1, 0]
    dj = [0, -1, 0, 1]

    now = way.popleft()

    for k in range(4):
        ni = now[0] + di[k]
        nj = now[1] + dj[k]
        if 0 <= ni < N and 0 <= nj < N and sea[ni][nj] <= shark_size:




N = int(input())
sea = [list(map(int, input().split())) for _ in range(N)]

# 처음 아기상어 위치
shark_i, shark_j = 0, 0
for i in range(N):
    for j in range(N):
        if sea[i][j] == 9:
            shark_i, shark_j = i, j

shark_size = 2
time = 0
bfs(shark_i, shark_j)