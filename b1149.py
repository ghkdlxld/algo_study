import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
cost = [list(map(int, input().split())) for _ in range(N)]

ans = int(1e9)
dp = [[]*3 for _ in range(N)]

print(dp)

def home(x):
    for k in range(3):
        if x


home(1)