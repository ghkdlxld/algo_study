import sys
sys.stdin = open('input.txt')


def fibo(x):
    if dp[x]:
        return dp[x]

    else:
        dp[x] = fibo(x-1) + fibo(x-2)
        return dp[x]

n = int(input())
arr = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597]
dp = [False]*91
for a in range(len(arr)):
    dp[a] = arr[a]

print(fibo(n))
