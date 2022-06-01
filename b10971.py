def trip(start, x):
    global result, cost
    if visited.count(0) == 0:
        # 돌아가는 길이 있는지 없는지 확인!!!
        if W[x][start] != 0:
            if result > cost + W[x][start]:
                result = cost + W[x][start]
        return

    if cost > result:
        return

    else:
        for i in range(N):
            # 방문하지 않았고, 연결되어 있으면
            if visited[i] == 0 and W[x][i] != 0:
                visited[i] = 1
                cost += W[x][i]
                trip(start, i)  # i로 이동

                visited[i] = 0
                cost -= W[x][i]


N = int(input())
W = [list(map(int, input().split())) for _ in range(N)]
result = 987654321

for n in range(N):
    visited = [0] * N
    visited[n] = 2
    cost = 0
    trip(n, n)

print(result)
