import sys
sys.stdin = open('input.txt')

def make_paper(i, j, k):
    visited[i][j] = 1
    k=1
    while True:
      pass
 
N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
blue = 0
white = 0

for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            if paper[i][j] == 1:
                blue += 1
            else:
                white += 1
            make_paper(i, j, 0)



print(visited)
