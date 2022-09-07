import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

INF = int(1e9)
def bfs(i, j):
    q = deque()
    q.append((i, j, 0))
    visited[0][0] = [0, 0]
    di = [0, 0, -1, 1]
    dj = [1, -1, 0, 0]

    while q:
        x, y, f = q.popleft()

        for k in range(4):
            ni = x + di[k]
            nj = y + dj[k]

            if 0 <= ni <N and 0 <= nj <M and board[ni][nj]+f < 2:
                go = visited[ni][nj][board[ni][nj]+f]
                now = visited[x][y][f]
                if now + 1 < go:
                    q.append((ni, nj, board[ni][nj]+f))
                    visited[ni][nj][board[ni][nj] + f] = now + 1



N, M = map(int, input().split())
board = [list(map(int, input().strip())) for _ in range(N)]
visited = [[[INF]*2 for _ in range(M)] for _ in range(N)]

bfs(0,0)
print(min(visited[N-1][M-1])+1 if min(visited[N-1][M-1])+1 < INF else -1)