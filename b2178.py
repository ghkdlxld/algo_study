import sys
sys.stdin = open('input.txt')
from collections import deque

def bfs():
    q = deque()
    q.append((0, 0))
    di = [0, 0, 1, -1]
    dj = [1, -1, 0, 0]

    while q:
        now = q.popleft()
        visited[now[0], now[1]] = 1
        for k in range(4):
            ni = now + di[k]
            nj = now + dj[k]



N, M = map(int, input().split()) # 1 ~ N , 1 ~ M
miro = [list(map(int, list(input()))) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

bfs()