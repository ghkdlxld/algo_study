import sys
sys.stdin = open('input.txt')
from collections import deque


def bfs(i, j):
    global beer
    q = deque((i, j))
    visited[i][j] = 1

    while q:
        di = [0, 0, 1, -1]
        dj = [1, -1, 0, 0]
        now_i, now_j = q.popleft()


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
