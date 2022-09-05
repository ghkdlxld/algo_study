import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
in_lst = list(map(int, input().split()))
post_lst = list(map(int, input().split()))
pre_lst = []
visited = [False]*(n+1)

def check_root(arr):
    x = -1
    for a in arr:
        if not visited[a] and post_lst.index(a) >= x:
            x = post_lst.index(a)

    if x >= 0:
        return arr.index(post_lst[x])
    else:
        return -1

def pre_order(arr):
    root = check_root(arr)
    if root >= 0:
        visited[arr[root]] = True
        pre_lst.append(arr[root])

        if len(arr) > 1:
            pre_order(arr[:root])
            pre_order(arr[root+1:])

pre_order(in_lst)
print(*pre_lst)



