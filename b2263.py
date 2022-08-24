import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
in_order_ans = list(map(int, input().split()))
post_order_ans = list(map(int, input().split()))
pre_order_ans = []

def pre_order(s, e):
    if e-s < 1:
        pre_order_ans.append(post_order_ans[s])
        return
    pre_order_ans.append(post_order_ans[e])
    x = in_order_ans.index(post_order_ans[e])
    y = post_order_ans.index(in_order_ans[x+1])
    pre_order(0, x-1)
    pre_order(y, y-e)

pre_order_ans.append(post_order_ans[-1])
x = in_order_ans.index(post_order_ans[-1])
y = post_order_ans.index(in_order_ans[x+1])
pre_order(0, x-1)
pre_order(y, n-1)
print(pre_order_ans)



