import sys, copy
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
sea = [list(map(int, input().split())) for _ in range(N)]
baby = [0, 0, 2]
time = 0

print(sea)


for x in range(N):
    for y in range(N):
        if sea[x][y] == 9:
            baby[0], baby[1] = x, y # 아기상어 위치

print(baby)

# 먹을 수 있는 물고기 찾기
can_eat = []
def eat():
    for i in range(N):
        for j in range(N):
            if sea[i][j] < baby[2]:
                can_eat.append([i, j, abs(i-baby[0])+abs(j-baby[1])]) # i,j, 거리


# r,c 에서 시작해서 baby[0], baby[1]까지 이동 가능여부, visited 필요
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
def can_go(r, c, visited):
    # 이동 가능 -> 이동
    q = deque([r,c])

    visited[r][c] = 1

    while q:
        now_i, now_j = r, c

        for k in range(4):
            ni = now_i + di[k]
            nj = now_j + dj[k]

            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] <= baby[2]: # visited 범위 수정 필요
                pass


    # 이동 불가능
    pass




while True:
    eat()
    # 더이상 먹을 수 있는 고기가 없으면
    if len(can_eat) == 0:
        break

    # 먹을 수 있는 물고기 중 거리가 가까운 순
    can_eat = sorted(can_eat, key=lambda x : [x[2], x[0], x[1]])

    for a, b, c in can_eat:
        # 먹으러 갈 수 있으면
        if can_go(a, b, copy.deepcopy(sea)):
            # 그 위치로 이동, 물고기 먹기, can_eat 초기화
            baby = [a, b, baby[2]+sea[a][b]]
            can_eat = []
            break

print(time)