import sys
input=sys.stdin.readline

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
ans = [0, 0]

def make_paper(x, y, N):
    color = paper[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if color != paper[i][j]:
                make_paper(x, y, N//2)
                make_paper(x+N//2, y, N//2)
                make_paper(x, y+N // 2, N // 2)
                make_paper(x+N//2, y + N // 2, N // 2)
                return
    ans[color] += 1

make_paper(0,0,N)
print(ans[0])
print(ans[1])