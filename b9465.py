import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    sticker = [list(map(int, input().split())) for _ in range(2)]


    dp = [[0]*n for _ in range(2)]
    dp[0][0] = sticker[0][0]
    dp[1][0] = sticker[1][0]

    print(sticker)
    print(dp)
    for i in range(2):
        for j in range(1, n):
            dp[i][j] = max()
