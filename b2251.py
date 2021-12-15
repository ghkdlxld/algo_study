import sys
import copy
sys.stdin = open('input.txt')

def dfs(x, state, cnt):
    if cnt != 0 and state in history:
        history.remove(state)
        return

    history.append(copy.deepcopy(state))

    if state[0] == 0 and state[2] not in ans:
        ans.append(state[2])

    for i in range(3):
        if state[i] != bottles[i] and i != x:
            if bottles[i] - state[i] > state[x]:
                state[i] += state[x]
                state[x] = 0
            else:
                state[x] -= bottles[i] - state[i]
                state[i] = bottles[i]
            dfs(i, state, cnt +1)




A, B, C = map(int, input().split())
bottles = [A, B, C]
ans = []
history = []
dfs(2, [0, 0, C], 0)
print(sorted(ans))