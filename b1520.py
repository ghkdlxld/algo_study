import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def dfs(i, j):
    stack = []
    stack.append([i,j])

    di = [0,0,1,-1]
    dj = [1, -1, 0, 0]






M, N = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(M)]
print(A)

dfs(0,0)