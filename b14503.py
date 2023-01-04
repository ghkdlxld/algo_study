import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dir = {0: [-1,0], 1:[0,-1], 2:[1,0], 3:[0,1]}
cnt = 0

print(arr)

def clean(i, j, d):
    # 현 위치 청소 -> 방문하지 않은 경우만 cnt += 1

    # d 기준 왼쪽부터 탐색 for

    # 청소 가능 -> (d+1)%4로 회전, 전진 재귀, break
    # 청소 불가능 -> (d+1)%4로 회전 재귀, break

    # for를 다 돌아서 d 로 제자리로 온 경우
    # 후진 가능 -> (d+2)%4로 전진(후진) d 그대로 재귀
    # 후진 불가능 -> return


