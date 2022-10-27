import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
square = [list(map(int, input().split())) for _ in range(n)]
d = [[] for _ in range(n)]
d[0].append(square[0][0])

for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            d[i].append(d[i-1][0]+square[i][0])
        elif j < i:
            d[i].append(max(d[i-1][j-1]+square[i][j], d[i-1][j]+square[i][j]))
        else:
            d[i].append(d[i-1][-1]+square[i][-1])

print(max(d[-1]))