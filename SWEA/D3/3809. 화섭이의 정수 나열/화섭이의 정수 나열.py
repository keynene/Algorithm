for T in range(int(input())):
  N = int(input())
  arr = []

  while len(arr) < N:
    arr += list(map(str, input().split()))

  num = ''
  for i in range(N):
    num += arr[i]
    
  res = set()
  ans = -1
  cnt = 1

  while ans < 0:
    for i in range(N):
      if i+cnt <= N:
        res.add(int(num[i:i+cnt]))
    
    for n in range(10**cnt):
      if n not in res:
        ans = n
        break
    cnt += 1

  print(f'#{T+1} {ans}')