import sys
sys.stdin = open('input.txt')

N, M, V = map(int, input().split())
line = [list(map(int, input().split())) for _ in range(M)]
print(line)