import sys, copy
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

M, N, H = map(int, input().strip().split())
tomato = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
visited = [[[0]*M for _ in range(N)] for _ in range(H)]

nh = [1, -1, 0, 0, 0, 0]
ny = [0, 0, 1, -1, 0, 0]
nx = [0, 0, 0, 0, 1, -1]

def check_left(chk):
    for h in range(H):
        for y in range(N):
            for x in range(M):
                if visited[h][y][x] == 0 and tomato[h][y][x] not in (1, -1):
                    chk += 1
    return chk

def bfs(cnt):
    q = deque()
    for z in range(H):
        for y in range(N):
            for x in range(M):
                if tomato[z][y][x] == 1 and visited[z][y][x] != 1:
                    q.append((z, y, x))
                    visited[z][y][x] = 1

    if len(q) > 0:
        while True:
            tmp = deque()
            while q:
                now_h, now_y, now_x = q.popleft()
                for k in range(6):
                    new_h, new_y, new_x = now_h+nh[k], now_y+ny[k], now_x+nx[k]
                    if 0 <= new_h < H and 0 <= new_y < N and 0 <= new_x < M and tomato[new_h][new_y][new_x] != -1 and visited[new_h][new_y][new_x] != 1:
                        tmp.append((new_h, new_y, new_x))
                        visited[new_h][new_y][new_x] = 1

            if len(tmp) < 1:
                if check_left(0) == 0: return cnt
                else: return -1

            else:
                cnt += 1
                q = tmp

    else:
        if check_left(0) == 0: return 0
        else: return -1


print(bfs(0))