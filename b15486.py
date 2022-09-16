import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
table = [[0, 0]] + [list(map(int, input().split())) for _ in range(N)]
dp = [0]*(N+1)
for i in range(1, N+1):
    if i+table[i][0]-1 <= N:
        dp[i+table[i][0]-1] = max(dp[i-1]+table[i][1], dp[i+table[i][0]-1])
    dp[i] = max(dp[i-1], dp[i])

print(dp[-1])