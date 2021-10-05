import sys
sys.stdin = open('input.txt')

def trip(x, cost):
    visited.append(x)
    if len(visited) == N:
        cost += W[x][visited[0]]
        visited.clear()
        return trip_min.append(cost)
    else:
        next = []
        for j in range(1, N+1):
            if (W[x][j] != 0) and (j not in visited):
                next.append(j)

        while next:
            b = next.pop(0)
            trip(b, cost + W[x][b])
            return -1


N = int(input())
W = [[0] + list(map(int, sys.stdin.readline().split())) for _ in range(N)]
W.insert(0, [0]*(N+1))
visited = []
trip_min = []
for i in range(1, N+1):
    trip_min.append(trip(i, 0))
for _ in range(trip_min.count(-1)):
    trip_min.remove(-1)
print(min(trip_min))