import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
stair = [int(input()) for _ in range(n)]
dp = [[0,0] for _ in range(n)]


if n < 2:
    print(sum(stair))

else:
    dp[0] = [stair[0], 0]
    dp[1] = [stair[0]+stair[1], stair[0]]

    for i in range(2, n):
        dp[i][0] = max(dp[i-2][1]+stair[i-1]+stair[i], dp[i-1][1]+stair[i])
        dp[i][1] = dp[i-1][0]

    print(dp[-1][0])