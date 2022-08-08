import sys
from collections import deque
sys.stdin = open('input.txt')

N, M = map(int, input().split())
board = [0]*101
visited = [987654321]*101
for i in range(N+M):
    a, b = map(int, input().split())
    board[a] = b

def bfs(x):
    q = deque()
    q.append(x)
    visited[x] = 0

    while q:
        now = q.popleft()
        for k in range(1, 7):
            if now+k > 100:
                break

            elif board[now+k] != 0:
                if visited[board[now + k]] > visited[now] + 1:
                    q.append(board[now+k])
                    visited[board[now + k]] = visited[now] + 1
            else:
                if visited[now+k] > visited[now] + 1:
                    q.append(now+k)
                    visited[now+k] = visited[now] + 1

bfs(1)
print(visited[100])