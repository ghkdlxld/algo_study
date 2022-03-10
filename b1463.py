import sys
sys.stdin = open('input.txt')

# dp 사용
def make_one(n):
    for i in range(2, n+1):
        ans[i] = ans[i-1] + 1
        if i%3 == 0:
            ans[i] = min(ans[i], ans[i // 3] + 1)

        if i%2 == 0:
            ans[i] = min(ans[i], ans[i // 2] + 1)


N = int(input())
ans = [0]*(N+1)
make_one(N)
print(ans[N])

# pypy3 으로 통과
def make_one(n, cnt):
    global ans

    if n == 1 and cnt < ans:
        ans = cnt
        return
    if n < 1 or cnt > ans:
        return


    else:
        if n%3 == 0:
            make_one(n//3, cnt+1)
        if n%2 == 0:
            make_one(n//2, cnt+1)
        make_one(n-1, cnt+1)



N = int(input())
ans = 9999999999
make_one(N, 0)
print(ans)