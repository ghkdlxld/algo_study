import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0
# 좌 하 우 상
di = [0, +1, 0, -1]
dj = [-1, 0, +1, 0]
ratio = [1, 0, 1, 2, 7, 0, 7, 2, 10, 0, 10, 5]

def tornado_dust(i, j, c):
    global ans
    y = arr[i+di[c]][j+dj[c]]
    t = 0
    total = 0

    x = int(y * 0.01 * ratio[t])
    for a in range(-1, 2, 1):
        if x > 0:
            if c%2 == 0 and 0 <= i+a < N:
                arr[i+a][j] += x
            elif c % 2 == 1 and 0 <= j+a < N:
                arr[i][j+a] += x
            else:
                ans += x

        total += x
        t += 1
        x = int(arr[i + di[c]][j + dj[c]] * 0.01 * ratio[t])

    for b in range(-2, 3, 1):
        if x > 0:
            if c % 2 == 0 and 0 <= i + b < N and 0 <= j+dj[c] < N:
                arr[i + b][j+dj[c]] += x
            elif c % 2 == 1 and 0 <= i+di[c] < N and 0 <= j + b < N:
                arr[i+di[c]][j + b] += x
            else:
                ans += x

        total += x
        t += 1
        x = int(arr[i + di[c]][j + dj[c]] * 0.01 * ratio[t])

    for d in range(-1, 2, 1):
        if x > 0:
            if c % 2 == 0 and 0 <= i + d < N and 0 <= j+dj[c]*2 < N:
                arr[i + d][j+dj[c]*2] += x
            elif c % 2 == 1 and 0 <= j + d < N and 0 <= i+di[c]*2 < N:
                arr[i+di[c]*2][j + d] += x
            else:
                ans += x

        total += x
        t += 1
        x = int(arr[i + di[c]][j + dj[c]] * 0.01 * ratio[t])

    # 5%
    if c % 2 == 0 and 0 <= j+dj[c] * 3 < N:
        arr[i][j+dj[c] * 3] += x
    elif c % 2 == 1 and 0 <= i+di[c] * 3 < N:
        arr[i+di[c] * 3][j] += x
    else:
        ans += x
    total += x


    # alpha
    x = int(y-total)
    if c % 2 == 0 and 0 <= j + dj[c]*2 < N:
        arr[i][j + dj[c]*2] += x

    elif c % 2 == 1 and 0 <= i + di[c]*2 < N:
        arr[i + di[c]*2][j] += x

    else:
        ans += int(y - total)

    arr[i + di[c]][j + dj[c]] = 0



def tornado_move(w, v, c, d, m):
    tornado_dust(w, v, c)

    if w == 0 and v == 0:
        return

    elif m != d-1:
        tornado_move(w+di[c], v+dj[c], c, d, m+1)

    else:
        if c%2 == 1:
            tornado_move(w + di[c], v + dj[c], (c+1)%4, d+1, 0)
        else:
            tornado_move(w + di[c], v + dj[c], (c + 1) % 4, d, 0)



tornado_move(N//2, N//2, 0, 1, 0)
print(ans)
