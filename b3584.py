import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10**9)

# 돌다가 A랑 겹치는게 있으면 return!!!!!
def find_josang(s, lst):
    lst.append(s)
    for i in range(1, N+1):
        if s in tree[i]:
            return find_josang(i, lst)
    return lst


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = [[] for _ in range(N + 1)]
    for n in range(N-1):
        A, B = map(int, input().split())
        tree[A].append(B)
    a, b = map(int, input().split())

    # A -> root
    A_way = []
    find_josang(a, A_way)

    # B -> root
    B_way = []
    find_josang(b, B_way)


    # 가장 먼저 겹치는 노드 찾기
    same_node = []
    for i in A_way:
        if same_node:
            break
        else:
            for j in B_way:
                if i == j:
                    same_node.append(i)
                    break
    print(*same_node)



