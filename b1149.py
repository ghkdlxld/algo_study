import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
cost = [list(map(int, input().split())) for _ in range(N)]

ans = int(1e9)
dp = [[0]*3 for _ in range(N)]
ans = 0

def home(x):
    for k in range(3):
        if dp[x][k] == 0:
            home(x+1)


home(1)

