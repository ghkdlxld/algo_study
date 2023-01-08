import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
students = [[] for _ in range(N**2+1)]
for x in range(N**2):
    tmp = list(map(int, input().split()))
    students[tmp[0]] = tmp[1:]

print(students)