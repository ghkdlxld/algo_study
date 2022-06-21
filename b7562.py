import sys
sys.stdin = open('input.txt')


def dfs(i, j):
    # 이동 가능 위치
    way = []
    way.append([i, j])

    di = []
    dj = []

    while way:




T = int(input())
for tc in range(1, T+1):
    N = int(input())
    now_i, now_j = map(int, input().split())
    goal_i, goal_j = map(int, input().split())


