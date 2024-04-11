import sys
from collections import deque
sys.stdin = open('input.txt')


def bfs(x, y):
    q = deque()
    q.append([x,y])


    while q:
      i, j = q.popleft()

      for k in range(4):
        ni, nj = i + di[k], j + dj[k]
        if 0 < ni <= N and 0 < nj <= M and arr[ni][nj] != 0 and ans[ni][nj] == 0:
            q.append([ni, nj])
            ans[ni][nj] = ans[i][j] + 1


N, M = map(int, input().split())
arr = [[0]*(M+1)] + [[0]+list(map(int, input())) for _ in range(N)]
ans = [[0]*(M+1) for _ in range(N+1)]
ans[1][1] = 1

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

bfs(1,1)
print(ans[N][M])