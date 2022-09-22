import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())
for tc in range(1, T+1):
    K = int(input())
    paper = list(map(int, input().split()))
    dp = [0]*K

