import sys
sys.stdin = open('input.txt')
from collections import deque
input = sys.stdin.readline

def bfs():
    q = deque()
    q.append((0, 0))
    visited[0][0] = 1
    di = [0, 0, 1, -1]
    dj = [1, -1, 0, 0]

    while q:
        now = q.popleft()
        for k in range(4):
            ni = now[0] + di[k]
            nj = now[1] + dj[k]

            if 0 <= ni < N and 0 <= nj < M and miro[ni][nj] == 1 and visited[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = visited[now[0]][now[1]] + 1
                if ni == N - 1 and nj == M - 1:
                    return visited[ni][nj]

N, M = map(int, input().split())
miro = [list(map(int, list(input().strip()))) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
ans = bfs()
print(ans)