import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0
# 좌 하 우 상
di = [0, +1, 0, -1]
dj = [-1, 0, +1, 0]
ratio = [1, 0, 1, 2, 7, 7, 2, 10, 0, 10, 5]

def tornado_dust(i, j, c):
    global ans
    t = 0
    total = 0

    x = int(arr[i+di[c]][j+dj[c]] * 0.01 * ratio[t])
    for a in range(-1, 2, 1):
        if x > 0:
            if 0 <= i+a < N and 0 <= j+a < N:
                if c%2 == 0:
                    arr[i+a][j] += x
                else:
                    arr[i][j+a] += x
            else:
                ans += x

        total += x
        x = int(arr[i + di[c]][j + dj[c]] * 0.01 * ratio[t + 1])

    for b in range(-2, 3, 1):
        if x > 0:
            if 0 <= i + b < N and 0 <= i+di[c] < N and 0 <= j+dj[c] < N and 0 <= j + b < N:
                if c % 2 == 0:
                    arr[i + b][j+dj[c]] += x
                else:
                    arr[i+di[c]][j + b] += x
            else:
                ans += x

        total += x
        x = int(arr[i + di[c]][j + dj[c]] * 0.01 * ratio[t + 1])

    for d in range(-1, 2, 1):
        if x > 0:
            if 0 <= i + d < N and 0 <= j + d < N and 0 <= j+dj[c]*2 < N and 0 <= i+di[c]*2 < N:
                if c % 2 == 0:
                    arr[i + d][j+dj[c]*2] += x
                else:
                    arr[i+di[c]*2][j + d] += x
            else:
                ans += x

        total += x
        x = int(arr[i + di[c]][j + dj[c]] * 0.01 * ratio[t + 1])

    if 0 <= j+dj[c] * 3 < N and 0 <= i+di[c] * 3 < N:
        if c % 2 == 0:
            arr[i][j+dj[c] * 3] += x
        else:
            arr[i+di[c] * 3][j] += x
    else:
        ans += x

    total += x

    if 0 <= i + b < N and 0 <= i + di[c] < N and 0 <= j + dj[c] < N and 0 <= j + b < N:
        if c % 2 == 0:
            arr[i][j + dj[c]] += int(arr[i+di[c]][j+dj[c]] - total)
        else:
            arr[i + di[c]][j] += int(arr[i+di[c]][j+dj[c]] - total)
    else:
        ans += int(arr[i+di[c]][j+dj[c]] - total)




def tornado_move(i, j, c, d, m):
    tornado_dust(i, j, c)
    arr[i+di[c]][j+dj[c]] = 0

    if i == 0 and j == 0:
        return

    elif m != d-1:
        tornado_move(i+di[c], j+dj[c], c, d, m+1)

    else:
        if c%2 == 1:
            tornado_move(i + di[c], j + dj[c], (c+1)%4, d+1, 0)
        else:
            tornado_move(i + di[c], j + dj[c], (c + 1) % 4, d, 0)



tornado_move(N//2, N//2, 0, 1, 0)
print(ans)
