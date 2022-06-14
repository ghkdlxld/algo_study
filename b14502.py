import sys
sys.stdin = open('input.txt')
from itertools import combinations
import copy
from collections import deque
input = sys.stdin.readline

def bfs(virus_map, g):
    q = deque()
    q.append

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
wall = []
for i in range(N):
    for j in range(M):
        wall.append((i, j))
group = list(combinations(range(N*M), 3))

for g in group:
    bfs(copy.deepcopy(arr), g)