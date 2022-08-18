import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

INF = int(1e9)
n = int(input())
graph = [[INF]*(n+1) for _ in range(n+1)]

for _ in range(n-1):
    s, e, w = map(int, input().split())
    graph[s][e] = w
    graph[e][s] = w

for a in range(n+1):
    for b in range(n+1):
        if a == b:
            graph[a][b] = 0

print(graph)
dist = [0*(n+1) for _ in range(n+1)]

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            dist[a][b] = max()