import sys
sys.stdin = open('input.txt')

def kill_node(k):
    global leaf
    if k in leaf:
        leaf.remove(k)
        if len(node_tree[tree[k]]) == 1:
            leaf.append(tree[k])
            for i in range(len(node_tree)):
                if node_tree[i] == [tree[k]]:
                    k = i
                    break

    if len(node_tree[k]) == 0:
        return
    if tree[k] == -1 and k == kill:
        leaf = []
        return

    else:
        for i in range(len(node_tree[k])):
            kill_node(node_tree[k][i])


N = int(input())
tree = list(map(int, sys.stdin.readline().split()))
kill = int(input())

node_tree = [[] for _ in range(N)]
for i in range(N):
    if tree[i] == -1:
        continue
    node_tree[tree[i]].append(i)
leaf = []
for x in range(N):
    if not node_tree[x]:
        leaf.append(x)
kill_node(kill)
print(len(leaf))
