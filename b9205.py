import sys
sys.stdin = open('input.txt')
from collections import deque


def bfs(i, j):
    global beer, walk, state
    q = deque()
    q.append((i, j))
    visited[i][j] = 1

    while q:
        # if walk == 50:
        #     walk = 0
        #     beer -= 1
        #
        # di = [0, 0, 1, -1]
        # dj = [1, -1, 0, 0]
        # now_i, now_j = q.popleft()
        # walk += 1
        #
        # if [now_i, now_j] == rock:
        #     if beer > 0:
        #         state = 'happy'
        #
        # if visited[now_i][now_j] == 2:
        #     beer = 20
        #
        # for k in range(4):
        #     ni = now_i + di[k]
        #     nj = now_j + dj[k]
        #     if 0<= ni< 32768 and 0<= nj< 32768 and visited[ni][nj] == 0:
        #         q.append((ni, nj))
        #         visited[ni][nj] = 1




T = int(input())
for tc in range(1, T+1):
    n = int(input())
    home = list(map(int, input().split()))
    store = [list(map(int, input().split())) for _ in range(n)]
    rock = list(map(int, input().split()))
    visited = [[0]*32768 for _ in range(32768)]

    for x in range(n):
        visited[store[x][0]][store[x][1]] = 2

    state = 'sad'
    beer = 20
    walk = 0
    bfs(home[0], home[1])

    print(state)