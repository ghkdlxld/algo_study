import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M, K = map(int, input().split())
fireball = [list(map(int, input().split())) for _ in range(M)]
print(fireball)