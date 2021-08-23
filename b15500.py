N = int(input())
s1 = list(map(int, input().split()))
s2 = []
s3 = []
order = []


for n in range(N, 0, -1):
    if n in s1:
        for s in s1[-1::-1]:
            if s != n:
                a = s1.pop(-1)
                s2.append(a)
                order.append([1, 2])
                continue
            a = s1.pop(-1)
            s3.append(a)
            order.append([1, 3])
            break

    elif n in s2:
        for s in s2[-1::-1]:
            if s != n:
                a = s2.pop(-1)
                s1.append(a)
                order.append([2, 1])
                continue
            a = s2.pop(-1)
            s3.append(a)
            order.append([2, 3])
            break


print(len(order))
for i in order:
    print(*i)

