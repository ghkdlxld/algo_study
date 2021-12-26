import sys
sys.stdin = open('input.txt')
from collections import deque

def bfs(i, j):
    global state, n
    q = deque()
    q.append((i, j))

    while q:
        now_i, now_j = q.popleft()
        for i in range(n):
            if now_i != stores[i][0] or now_j != stores[i][1]:
                if abs(stores[i][0] - now_i) + abs(stores[i][1] - now_j) <= 1000:
                    if abs(rock[0]-stores[i][0]) + abs(rock[1]-stores[i][1]) <= 1000:
                        state = 'happy'
                        return

                    # 처음에 visited 말고 not in 을 썼더니 시간초과가 뜸
                    if visited[i] == 0:
                        q.append(stores[i])
                        visited[i] = 1


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    home = list(map(int, input().split()))
    stores = [list(map(int, input().split())) for _ in range(n)]
    rock = list(map(int, input().split()))
    visited = [0]*n

    state = 'sad'
    if abs(rock[0] - home[0]) + abs(rock[1] - home[1]) <= 1000:
        state = 'happy'
    else:
        bfs(*home)
    print(state)
