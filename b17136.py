import sys
sys.stdin = open('input.txt')




board = [list(map(int, input().split())) for _ in range(10)]
paper = [1, 2, 3, 4, 5]
paper_cnt = [0]*6
