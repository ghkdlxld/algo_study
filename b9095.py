# A(n-1), 즉 n-1을 만드는 모든 경우 각각에 대해 그 뒤에 1을 더하는 것
# A(n-2), 즉 n-2를 만드는 모든 경우 각각에 대해 그 뒤에 2를 더하는 것
# A(n-3), 즉 n-3을 만드는 모든 경우 각각에 대해 그 뒤에 3을 더하는 것

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
dp = [0, 1, 2, 4, 7] + [False]*6

def plus(x):
    if dp[x]:
        return dp[x]
    else:
        dp[x] = plus(x-3) + plus(x-2) + plus(x-1)
        return dp[x]

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    print(plus(n))



