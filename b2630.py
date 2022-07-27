import sys
sys.stdin = open('input.txt')

# 시작점 i,j 변의 길이 m, 색깔
# True 모두 같음
def same(i, j, m, k):
    for x in range(i, i+m):
        for y in range(j, j+m):
            if paper[x][y] != k:
                return False
    return True

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
print(paper)
stack = [(0, 0, N)]


