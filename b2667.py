import sys
sys.stdin = open('input.txt')

def dfs():
    di = [-1, 0, 0, 1]
    dj = [0, 1, -1, 0]
    area = 0
    while stack:
        now = stack.pop(0)
        visited[now[0]][now[1]] = 1
        area += 1
        for k in range(4):
            ni = now[0] + di[k]
            nj = now[1] + dj[k]
            if (0 <= ni < N) and (0 <= nj < N) and (visited[ni][nj] == 0) and (board[ni][nj] == 1) and ([ni, nj]not in stack):
                stack.append([ni, nj])
    return area


N = int(input())
board = [list(map(int, input())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
stack = []
result = []
cnt = 0
for a in range(N):
    for b in range(N):
        if board[a][b] == 1 and visited[a][b] == 0:
            stack.append([a, b])
            cnt += 1
            result.append(dfs())

ans = sorted(result)
print(cnt)
for i in ans:
    print(i)