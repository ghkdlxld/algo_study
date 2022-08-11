# 순회 방식
import sys
input=sys.stdin.readline

V, E = map(int, input().split())
K = int(input())

INF = int(1e9)
graph = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append([v, w])


dist = [INF]*(V+1)
visited = [False]*(V+1)

# 인접한 노드 중 최단거리를 가지는 노드 반환
def get_smallest():
    min_value = (0, INF)
    for i in range(1, V+1):
        if not visited[i] and dist[i] < min_value[1]:
            min_value = (i, dist[i])
    return min_value[0]


def Dijkstra(start):
    dist[start] = 0
    visited[start] = True

    for (adj_node, weight) in graph[start]:
        # 같은 노드간 여러 간선이 존재할 수 있으므로 if 문을 써준다
        if dist[adj_node] > weight:
            dist[adj_node] = weight

    # 시작 노드를 제외한 다른 모든 노드를 순회
    for _ in range(V-1):
        # 인접 노드 중 최단거리 노드를 방문
        now = get_smallest()
        visited[now] = True

        # 기존의 최단거리(시작-인접node) > 현재 방문한 노드를 거친 최단거리(시작-now + now-인접node)
        # 일 경우 최단거리 테이블 갱신
        for (adj_node, weight) in graph[now]:
            cost = dist[now] + weight
            if cost < dist[adj_node]:
                dist[adj_node] = cost

Dijkstra(K)
for i in range(1,V+1):
    print(dist[i] if dist[i] < INF else 'INF')



# 우선순위 큐 사용
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