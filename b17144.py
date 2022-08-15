import sys
from collections import deque

sys.stdin = open('input.txt')
input = sys.stdin.readline

R, C, T = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(R)]
machine = []

for _ in range(T):
    dust = deque()
    for i in range(R):
        for j in range(C):
            if room[i][j] > 0:
                dust.append((i, j, room[i][j]))
            if room[i][j] == -1:
                machine.append(i)

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    diffuse = deque()
    while dust:
        r, c, A = dust.popleft()

        cnt = 0
        for k in range(4):
            nr = r + di[k]
            nc = c + dj[k]
            if 0 <= nr < R and 0 <= nc < C and room[nr][nc] >= 0:
                diffuse.append((nr, nc, A//5))
                cnt += 1

        room[r][c] = A-(A//5)*cnt

    while diffuse:
        r, c, A = diffuse.popleft()
        room[r][c] += A

    # 위
    # 왼쪽
    for x in range(machine[0]-1, 0, -1):
        room[x][0] = room[x-1][0]

    # 위

    for x in range(C-1):
        room[0][x] = room[0][x+1]

    # 오른쪽
    for x in range(machine[0]):
        room[x][-1] = room[x+1][-1]

    # 아래
    for x in range(C-1, 1, -1):
        room[machine[0]][x] = room[machine[0]][x-1]
    room[machine[0]][1] = 0

    # 아래
    # 왼
    for x in range(machine[1]+1, R-1):
        room[x][0] = room[x+1][0]

    # 아래
    for x in range(C-1):
        room[-1][x] = room[-1][x+1]

    # 오른
    for x in range(R-1, machine[1], -1):
        room[x][-1] = room[x-1][-1]

    # 위
    for x in range(C-1, 1, -1):
        room[machine[1]][x] = room[machine[1]][x-1]
    room[machine[1]][1] = 0


ans = 0
for i in range(R):
    ans += sum(room[i])
print(ans+2)
