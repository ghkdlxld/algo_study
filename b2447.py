import sys
sys.stdin = open('input.txt')

N = int(input())
star = [['*']*N for _ in range(N)]
n = N
while n != 1:
    for i in range(n//3, (n//3)*2):
        for x in range():
            for j in range(n//3, (n//3)*2):
                star[i][j] = ' '
    n = n//3


for n in range(N):
    print(''.join(star[n]))
