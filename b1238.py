import sys, heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline

INF = int(1e9)
N, M, X = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    s, e, t = map(int, input().split())
    graph[s].append([e, t])



def Dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    time[start] = 0

    while q:
        now_t, now_c = heapq.heappop(q)

        if time[now_c] < now_t:
            continue

        for (adj_node, delay) in graph[now_c]:
            total_t = now_t + delay

            if total_t < time[adj_node]:
                time[adj_node] = total_t
                heapq.heappush(q, (total_t, adj_node))

ans = [0]*(N+1)
for k in range(1, N+1):
    time = [INF] * (N + 1)
    Dijkstra(k)
    ans[k] += time[X]
    if k == X:
        for i in range(1, N+1):
            ans[i] += time[i]

print(max(ans))