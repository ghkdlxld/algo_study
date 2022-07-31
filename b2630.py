import sys
sys.stdin = open('input.txt')
from collections import deque

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
visited = [[0]*N for _ in range(N)]
ans = [0, 0]
q = deque()
q.append((0, 0))

m = N
while q:
    now = q.popleft()
    if same(*now, m, paper[now[0]][now[1]]):
        ans[paper[now[0]][now[1]]] += 1
        for a in range(m):
            for b in range(m):
                visited[now[0]+a][now[1]+b] = 1
    else:
        if q:

        m *= 2
        for a in range(2):
            for b in range(2):
                q.append((now[0]+(N//m+1)*a, now[1]+(N//m + 1)*b))




print(ans)
