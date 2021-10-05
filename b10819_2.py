import sys
sys.stdin = open('input.txt')



def dfs(x, i):
    stack = []
    stack.append(x)
    visited[i] = 1



N = int(input())
A = list(map(int, input().split()))
visited = [0]*N
for i in range(N):
    dfs(A[i],i)