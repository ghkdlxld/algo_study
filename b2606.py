import sys
sys.stdin = open('input.txt')

def virus(c):
    global link
    sick = []
    sick_com[c] = 1


    for j in range(len(link[c])):
        if (0 < j <= computer) and (sick_com[j] == 0) and (link[c][j] == 1) and (j not in sick):
            sick.append(j)

    for s in sick:
        virus(s)

computer = int(input())
link_num = int(input())
link = [[0]*(computer+1) for _ in range(computer+1)]
sick_com = [0]*(computer+1)

for i in range(link_num):
    a, b = list(map(int, input().split()))
    link[a][b], link[b][a] = 1, 1


virus(1)
print(sum(sick_com)-1)

