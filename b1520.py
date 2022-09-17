import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

M, N = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(M)]
print(A)