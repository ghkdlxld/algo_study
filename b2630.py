import sys
sys.stdin = open('input.txt')

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]




print(paper)