# 원래는 dfs한번으로 O(n**2) 으로 풀었었다 -> 시간초과
# dfs 두번으로 O(n) 풀이 + setrecursion으로 통과
# 임의 한 노드 - 제일 먼 노드(n1), n1으로 부터 제일 먼 노드까지 거리 = 트리의 지름

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
 
n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    s, e, w = map(int, input().split())
    graph[s].append([e, w])
    graph[e].append([s, w])


def dfs(x, cnt, n):
    for node in graph[x]:
        if not visited[node[0]]:
            visited[node[0]] = True
            dfs(node[0], cnt+node[1], n)
        if dist[n][1] < cnt:
            dist[n][1] = cnt
            dist[n][0] = x

visited = [False]*(n+1)
visited[1] = True
# 노드, 거리
dist = [[0, 0], [0, 0]]
dfs(1, 0, 0)

visited = [False]*(n+1)
visited[dist[0][0]] = True
dfs(dist[0][0], 0, 1)
print(dist[1][1])
