import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque

def bfs():
    global cnt
    di =[0, 0, 1, -1]
    dj = [1, -1, 0, 0]

    while True:
        q = []

        while day[-1]:
            x, y = day[-1].pop()

            for k in range(4):
                ni = x + di[k]
                nj = y + dj[k]
                if 0 <= ni < N and 0<= nj < M and box[ni][nj] == 0 and visited[ni][nj] == 0:
                    q.append((ni, nj))
                    cnt += 1
                    visited[ni][nj] = 1

        if len(q) == 0:
            return
        day.append(q)


M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
day = [[]]
vacate_tomato = 0

for i in range(N):
    vacate_tomato += box[i].count(-1)
    for j in range(M):
        if box[i][j] == 1:
            visited[i][j] = 1
            day[0].append((i, j))

all_tomato = M*N - vacate_tomato
cnt = len(day[0])

if cnt == all_tomato:
    print(0)

else:
    bfs()
    if cnt != all_tomato:
        print(-1)
    else:
        print(len(day)-1)

