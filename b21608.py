import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
students = dict()
for x in range(N**2):
    tmp = list(map(int, input().split()))
    students[tmp[0]] = tmp[1:]

seat = [[0]*N for _ in range(N)]

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
ans = 0

def place_std(x, y):
    for i in range(N):
        for j in range(N):
            tmp = [i, j, 0, 0] # 현 위치 i, j / like, empty
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]

                if seat[i][j] == 0 and 0 <= ni < N and 0 <= nj < N:
                    if seat[ni][nj] == 0:
                        tmp[3] += 1
                    elif seat[ni][nj] in y:
                        tmp[2] += 1
            like_lst.append(tmp)



for k, v in students.items():
    like_lst = []
    place_std(k, v)
    like_lst = sorted(like_lst, key=lambda x:[-x[2], -x[3]])
    check_seat = like_lst[0]
    seat[check_seat[0]][check_seat[1]] = k



for a in range(N):
    for b in range(N):
        cnt = 0
        for k in range(4):
            na = a + di[k]
            nb = b + dj[k]

            if 0 <= na < N and 0 <= nb < N and (seat[na][nb] in students[seat[a][b]]):
                cnt += 1

        ans += int(10 ** (cnt - 1))

print(ans)