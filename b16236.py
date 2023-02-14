# 아기상어 위치부터 시작해서 먹을수 있는 후보군들 bfs 한번에 구하면 더 빠를듯
# 현재는 후보군들 구하고, 갈수있는지(bfs 후보군 갯수 만큼 돌게 됨...)
import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
sea = [list(map(int, input().split())) for _ in range(N)]
baby = [0, 0, 2]
eat_cnt = 0
time = 0


for x in range(N):
    for y in range(N):
        if sea[x][y] == 9:
            baby[0], baby[1] = x, y # 아기상어 위치
            sea[x][y] = 0   # 아기상어 위치 저장후 0 처리



# r,c 에서 시작해서 baby[0], baby[1]까지 이동 가능여부, visited 필요
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
def can_go(r, c, visited):
    # 이동 가능 -> 이동
    q = deque()
    q.append([r, c])

    while q:
        now = q.popleft()

        for k in range(4):
            ni = now[0] + di[k]
            nj = now[1] + dj[k]

            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0 and sea[ni][nj] <= baby[2]:
                visited[ni][nj] = visited[now[0]][now[1]] + 1
                q.append([ni, nj])

                if ni == baby[0] and nj == baby[1]:
                    return visited[ni][nj]
    return False




while True:
    can_eat = []
    for a in range(N):
        for b in range(N):
            if 0 < sea[a][b] < baby[2]: # 먹을 수 있으면
                v = [[0] * (N + 1) for _ in range(N)]
                d = can_go(a, b, v)
                if d:
                    can_eat.append([a, b, d])


    if len(can_eat) == 0:
        break

    can_eat = sorted(can_eat, key=lambda x: [x[2], x[0], x[1]])
    target = can_eat[0]

    # 그 위치로 이동, 물고기 먹기, can_eat 초기화
    baby = [target[0], target[1], baby[2]]
    eat_cnt += 1
    if eat_cnt == baby[2]:
        baby[2] += 1
        eat_cnt = 0

    sea[target[0]][target[1]] = 0 # 물고기가 이동한 위치
    time += target[2]  # 이동하기까지 시간



print(time)