import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import copy

M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]
visited = copy.deepcopy(box)

print(visited)