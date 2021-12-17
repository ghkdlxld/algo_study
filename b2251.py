import sys
sys.stdin = open('input.txt')

def bfs():
    pass




A, B, C = map(int, input().split())
bottles = [A, B, C]
ans = []
visited = [[0]*3 for _ in range(3)]
bfs()
print(sorted(ans))