import sys
sys.stdin = open('input.txt')
def snowman(snow, n, cnt):
    global result
    if n >= N or cnt >= M:
        if snow > result:
            result = snow
            return snow
        return
    else:
        if n <= N - 1:
            snowman(snow+a[n+1], n+1, cnt+1)
        if n <= N - 2:
            snowman(int(snow*0.5+a[n+2]), n+2, cnt+1)


N, M = map(int, sys.stdin.readline().split())
a = [0] + list(map(int, sys.stdin.readline().split()))
result = 0
snowman(1, 0, 0)
print(result)
