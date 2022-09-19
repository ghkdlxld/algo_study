import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def dfs(i, j):

    if i == M-1 and j == N-1:
        visited[i][j] += 1
        return

    di = [0, 0, 1, -1]
    dj = [1, -1, 0, 0]

    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]

        if 0 <= ni < M and 0 <= nj < N and A[ni][nj] < A[i][j]:
            dfs(ni, nj)



M, N = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(M)]
visited = [[0]*N for _ in range(M)]
dfs(0,0)
print(visited[-1][-1])