import sys
from collections import deque
sys.stdin = open('input.txt')

def pour(x, y):
    if visited[x][y] == 0:
        visited[x][y] = 1
        q.append([x, y])

def bfs():
    q.append([0, 0])
    visited[0][0] = 1

    while q:
        a, b = q.popleft()
        c = C - (a+b)
        if a == 0:
            ans.append(c)

        # x->y, x->z, y->x, y->z, z->x, z->y
        # 부을 때 A, B 물통 상태
        water = min(a, B - b)
        pour(a-water, b+water)

        water = min(a, C - c)
        pour(a-water, b)

        water = min(b, A - a)
        pour(a + water, b - water)

        water = min(b, C-c)
        pour(a, b-water)

        water = min(c, A-a)
        pour(a+water, b)

        water = min(c, B-b)
        pour(a, b+water)

A, B, C = map(int, input().split())
visited = [[0]*(B+1) for _ in range(A+1)]
q = deque()
ans = []
bfs()

print(' '.join(map(str, sorted(ans))))

