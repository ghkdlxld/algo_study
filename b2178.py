import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
miro = [list(map(int, list(input()))) for _ in range(N)]
print(miro)