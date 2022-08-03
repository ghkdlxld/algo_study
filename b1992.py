import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
media = [ list(map(int, input().strip())) for _ in range(N)]
arr = []
def solution(x, y, N, c):
    color = media[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if color != media[i][j]:
                solution(x, y, N//2, c + '0')
                solution(x, y+N//2, N // 2, c + '1')
                solution(x+N//2, y, N // 2, c+'2')
                solution(x+N//2, y+N//2, N // 2, c+'3')
                arr.append(')')
                return

    arr.append((color, c))

solution(0, 0, N, '')
print(arr)