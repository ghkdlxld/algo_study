import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def pre(n):
    print(n, end='')
    for x in graph[n]:
        if x != '.':
            pre(x)

def inorder(n):
    if graph[n][0] != '.':
        inorder(graph[n][0])
    print(n, end='')
    if graph[n][1] != '.':
        inorder(graph[n][1])


def postorder(n):
    for x in graph[n]:
        if x != '.':
            postorder(x)
    print(n, end='')



N = int(input())
graph = {}
for _ in range(N):
    root, l, r = input().split()
    graph[root] = [l, r]

pre('A')
print('')
inorder('A')
print('')
postorder('A')