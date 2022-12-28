import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dir = {0: [-1,0], 1:[0,-1], 2:[1,0], 3:[0,1]}
cnt = 0

# 왼쪽 (+1)%4