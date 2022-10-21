import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque

N = int(input())
space = [list(map(int, input().split())) for _ in range(N)]

print(space)

def fish(i, j, cnt):
    for k in range()



for i in range(N):
    for j in range(N):
        if space[i][j] == 9:
            fish(i, j, 0)