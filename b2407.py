import sys
sys.stdin = open('input.txt')

n, m = map(int, input().split())
t = 1
b = 1
for x in range(n, n-m, -1):
    t*=x
    b *= (n-x+1)
print(t//b)
