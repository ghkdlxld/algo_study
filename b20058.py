# python으로 시간초과나서 pypy로 통과

import sys
from collections import deque
import copy
input=sys.stdin.readline


# 회전
def rotate(L, N):
    a = [[0]*(2**N) for _ in range(2**N)]

    for i in range(0, 2**N, 2**L):
        for j in range(0, 2**N, 2**L):

            for r in range(2**L):
                for c in range(2**L):
                    a[i+c][j+2**L-1-r] = A[i+r][j+c]
    return a


# 인접칸 0 아닌 수 3개 미만이면 check
def ice_break(N, lst):
    check = copy.deepcopy(lst)
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    for i in range(2 ** N):
        for j in range(2 ** N):
            cnt = 0
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < (2**N) and 0 <= nj < (2**N):
                    if lst[ni][nj] != 0:
                        cnt += 1
            if cnt < 3 and lst[i][j] > 0:
                check[i][j] = lst[i][j] - 1
    return check

def firestorm(L, N):
    a = rotate(L, N)
    a = ice_break(N, a)
    return a

def dfs(i, j):
    global ans, tmp
    way = deque()
    way.append([i, j])

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    while way:
        now = way.popleft()
        for k in range(4):
            ni = now[0] + di[k]
            nj = now[1] + dj[k]
            if 0 <= ni < (2**N) and 0 <= nj < (2**N):
                if A[ni][nj] != 0:
                    way.append([ni, nj])
                    A[ni][nj] = 0
                    tmp += 1


N, Q = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(1<<N)]
L = list(map(int, input().split()))

for l in L:
    A = firestorm(l, N)

# 전체 합
cnt = 0
for i in range(2**N):
    cnt += sum(A[i])

# 가장 큰 덩어리
ans = 0
for i in range(2**N):
    for j in range(2**N):
        if A[i][j] != 0:
            tmp = 0
            dfs(i, j)
            if tmp > ans:
                ans = tmp

print(cnt)
print(ans)