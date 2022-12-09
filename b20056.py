import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M, K = map(int, input().split())
fireball = [list(map(int, input().split())) for _ in range(M)]
arr = [[[] for _ in range(N)] for _ in range(N)]
direction = [[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]]
curl = 0
cnt = 0

for r, c, m, s, d in fireball:
    arr[r-1][c-1].append([m, s, d])

def fire(new_arr):
    for i in range(N):
        for j in range(N):
            if len(arr[i][j]) > 0:
                for m, s, d in arr[i][j]:
                    r, c = direction[d]
                    new_arr[(i+r*s)%N][(j+c*s)%N].append([m, s, d])

    return new_arr


def divide(i, j):
    new_m = 0
    new_s = 0
    new_d = arr[i][j][0][2]%2
    flag = True
    for m, s, d in arr[i][j]:
        new_m += m
        new_s += s
        if flag and d%2 != new_d:
            flag = False

    new_m //= 5
    new_s //= len(arr[i][j])
    tmp = []

    if new_m > 0 and flag:
        for x in [0, 2, 4, 6]:
            tmp.append([new_m, new_s, x])
    elif new_m > 0:
        for y in [1, 3, 5, 7]:
            tmp.append([new_m, new_s, y])

    return tmp



while curl < K:
    curl += 1
    new_arr = [[[] for _ in range(N)] for _ in range(N)]
    arr = fire(new_arr)
    for i in range(N):
        for j in range(N):
            if len(arr[i][j]) > 1:
                arr[i][j] = divide(i, j)


for x in range(N):
    for y in range(N):
        t = 0
        for m in arr[x][y]:
            t += m[0]
        cnt += t

print(cnt)