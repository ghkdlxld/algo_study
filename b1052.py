N, K = map(int, input().split())
binary_num = bin(N)[2:]
cnt = 0
while binary_num.count('1') > K:
    binary_num = bin(int(binary_num, 2) + 1)[2:]
    cnt += 1
print(cnt)

# python으로 통과가 안돼서 pypy로 통과
# while 문 돌릴때 계속 1을 더하지 말고
# 1인 부분을 찾아서 그자리에 1<<n 을 더해주는 방법 하면 더 단축될 것 같음