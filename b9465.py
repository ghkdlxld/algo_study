import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    sticker = [list(map(int, input().split())) for _ in range(2)]
    print(sticker)