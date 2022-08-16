import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
visited = [0]*(N+1)
q = []

def sol(x):
    if len(q) == M:
        print(*q)
        return

    else:
        for k in range(x, N+1):
            if visited[k] != 1:
                visited[k] = 1
                q.append(k)
                sol(k+1)
                visited[k] = 0
                q.pop()


for i in range(1, N+1):
    visited[i] = 1
    q.append(i)
    sol(i)
    q.pop()