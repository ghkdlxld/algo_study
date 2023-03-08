import sys
sys.stdin = open('input.txt')

wheel = [list(map(int, input())) for _ in range(4)]
K = int(input())
spin = [list(map(int, input().split())) for _ in range(K)]

print(wheel)
print(spin)