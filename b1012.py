import sys
sys.setrecursionlimit(100000)

def worm(i, j):
    global M, N, cnt
    way = []
    way.append([i, j])

    # 우 하 좌 상
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    now = way.pop(0)
    bat[now[0]][now[1]] = 0
    for k in range(4):
        ni = now[0] + di[k]
        nj = now[1] + dj[k]
        if (0 <= ni < N and 0 <= nj < M) and bat[ni][nj] == 1:
            way.append([ni, nj])

    while way:
        go = way.pop(0)
        worm(go[0], go[1])



T = int(input())
for tc in range(1, T+1):
    M, N, K = map(int, input().split())
    bat = [[0]*M for _ in range(N)]
    for k in range(K):
        x, y = map(int, sys.stdin.readline().split())
        bat[y][x] = 1

    cnt = 0
    for i in range(N):
        for j in range(M):
            if bat[i][j] == 1:
                worm(i, j)
                cnt += 1

    print(cnt)