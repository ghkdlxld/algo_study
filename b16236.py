import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
sea = [list(map(int, input().split())) for _ in range(N)]

print(sea)