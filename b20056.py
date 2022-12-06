import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M, K = map(int, input().split())
fireball = [list(map(int, input().split())) for _ in range(M)]
arr = [[[] for _ in range(N)] for _ in range(N)]
direction = [[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]]
curl = 0

for r, c, m, s, d in fireball:
    arr[r-1][c-1].append([m, s, d])

# 이동
def fire(new_arr):
    for i in range(N):
        for j in range(N):
            if len(arr[i][j]) > 0:
                for m, s, d in arr[i][j]:
                    r, c = direction[d]
                    new_arr[(i+r*s)%N][(j+c*s)%N].append([m, s, d])

    return new_arr


# 합치고 나누기
def divide():
    # for a in arr:
    #     print(a, end='\n')
    for i in range(N):
        for j in range(N):
            if len(arr[i][j]) > 1:
                # m 합치기, 방향 확인(모두 홀수,짝수?),





if curl < K:
    curl += 1
    new_arr = [[[] for _ in range(N)] for _ in range(N)]
    arr = fire(new_arr)
    divide()
