import sys
sys.stdin = open('input.txt')

def make_paper():
    pass


N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
make_paper()

print(visited)