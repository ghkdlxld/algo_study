import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
media = [ list(map(int, input().strip())) for _ in range(N)]
ans = ''
def solution(x, y, N):
    global ans
    color = media[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if color != media[i][j]:
                ans += '('
                solution(x, y, N//2)
                solution(x, y+N//2, N // 2)
                solution(x+N//2, y, N // 2)
                solution(x+N//2, y+N//2, N // 2)
                ans += ')'
                return

    ans += str(color)

solution(0, 0, N)
print(ans) 
