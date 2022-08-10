import sys, heapq
sys.stdin = open('input.txt')
input=sys.stdin.readline

V, E = map(int, input().split())
K = int(input())

INF = int(1e9)
graph = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append([v, w])

dist = [INF]*(V+1)

def Dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0

    while q:
        current_d, now = heapq.heappop(q)
        if dist[now] < current_d:
            continue

        for (adj_node, weight) in graph[now]:
            total_d = current_d + weight
            if total_d < dist[adj_node]:
                dist[adj_node] = total_d
                heapq.heappush(q, (total_d, adj_node))

Dijkstra(K)
for i in range(1,V+1):
    print(dist[i] if dist[i] < INF else 'INF')