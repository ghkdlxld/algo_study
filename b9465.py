import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    sticker = [list(map(int, input().split())) for _ in range(2)]


    dp = [[0]*n for _ in range(2)]
    dp[0][0] = sticker[0][0]
    dp[1][0] = sticker[1][0]

    for j in range(1, n):
        for i in range(2):
            if j > 1:
                dp[i][j] = max(max(dp[0][j-2], dp[1][j-2])+sticker[i][j], dp[abs(i-1)][j-1]+sticker[i][j])
            else:
                dp[i][j] = dp[abs(i-1)][j-1]+sticker[i][j]

    print(max(dp[0][-1], dp[1][-1]))