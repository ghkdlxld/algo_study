tc=int(input())
for t in range(1, tc+1):
  n=int(input())
  arr=list(map(int,input().split()))
  ans=[]
  q=[]

  while len(arr)!=0:
    if len(q)==0 or q[0]!=arr[0]:
      ans.append(arr[0])
      q.append(int((arr[0]/3)*4))
    else:
      q.pop(0)
    arr.pop(0)

  print('Case #{}:'.format(t), *ans)