def solution(grid, k):
    answer = 987654321
    N = len(grid)
    M = len(grid[0])
    load = [list(grid[i]) for i in range(N)]
    visited = [[0] * M for i in range(N)]

    di = [0, 0, -1, 1]
    dj = [1, -1, 0, 0]

    def dfs(i, j, sleep, move, k):
        now = (i, j)
        visited[i][j] = 1
        move += 1

        if move == k:
            if load[now[0]][now[1]] == '.':
                sleep += 1
                move = -1
            else:
                return

        if now[0] == N - 1 and now[1] == M - 1 and tmp < ans:
            answer = sleep
            return

        for k in range(4):
            ni = now[0] + di[k]
            nj = now[1] + dj[k]

            if 0 <= ni < N and 0 <= nj < M and load[ni][nj] != '#' and visited[ni][nj] == 0:
                if load[ni][nj] == '.':
                    for x in [True, False]:
                        if x:
                            s = sleep = 1
                            m = move - 1
                        dfs(ni, nj, s, m, k)

                else:
                    dfs(ni, nj, sleep, move, k)
            return

    dfs(0, 0, 0, -1, k)

    return answer


