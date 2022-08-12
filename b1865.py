import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())
INF = int(1e9)

def floyd():
    for k in range(1, N+1):
        for a in range(1, N+1):
            for b in range(1, N+1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
                if a == b and graph[a][b] < 0:
                    return True
    return False

for tc in range(1, T+1):
    N, M, W = map(int, input().split())
    graph = [[INF] * (N+1) for _ in range(N+1)]
    for i in range(1, N+1):
        for j in range(1, N + 1):
            if i == j:
                graph[i][j] = 0

    for _ in range(M):
        S, E, T = map(int, input().split())
        graph[S][E] = min(graph[S][E], T)
        graph[E][S] = graph[S][E]


    for _ in range(W):
        S, E, T = map(int, input().split())
        graph[S][E] = min(graph[S][E], -T)

    print('YES' if floyd() else 'NO')
