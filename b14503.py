import sys
input = sys.stdin.readline

N, M = map(int, input().split())
r, c, d = map(int, input().split())
visited = [list(map(int, input().split())) for _ in range(N)]
dir = {0: [-1,0], 1:[0,1], 2:[1,0], 3:[0,-1]}
cnt = 0


def clean(i, j, d):
    global cnt
    # 현 위치 청소 -> 방문하지 않은 경우만 cnt += 1
    if visited[i][j] == 0:
        visited[i][j] = 2
        cnt += 1


    # d 기준 왼쪽부터 탐색 for
    for k in range(4):
        new_dir = (d + 3) % 4
        new_i = i+dir[new_dir][0]
        new_j = j+dir[new_dir][1]
        # 청소 가능 -> (d+1)%4로 회전, 전진 재귀, break
        if visited[new_i][new_j] == 0:
            clean(new_i, new_j, new_dir)
            return

        # 청소 불가능(벽/이미청소) -> (d+1)%4로 회전 재귀
        else:
            d = new_dir


    # for를 다 돌아서 d 로 제자리로 온 경우
    # 후진 가능(벽 아님) -> (d+2)%4로 전진(후진) d 그대로 재귀
    back_i = i + dir[(d+2)%4][0]
    back_j = j + dir[(d+2)%4][1]
    if visited[back_i][back_j] != 1:
        clean(back_i, back_j, d)


    # 후진 불가능 -> return
    return



clean(r, c, d)
print(cnt)