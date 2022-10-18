import sys
sys.stdin = open('input.txt')

N = int(input())
num = list(map(int, input().split()))
cal = list(map(int, input().split())) # +,-,*,//
visited = [0]*4
ans = 0

def sol(x, tmp):
    if x == N and tmp > ans:
        return

    for i in range(4):
        if cal[i]-visited[i] > 0:
            visited[i] += 1
            sol()





sol(0, num[0])