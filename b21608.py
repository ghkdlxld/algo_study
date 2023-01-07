import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
seat = [ list(map(int, input().split())) for _ in range(N**2)]

print(seat)