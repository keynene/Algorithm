for T in range(1,11):
  tc = int(input())
  comp = input().rstrip()
  lst = input().rstrip()
  cnt = 0

  L = len(comp)
  now = 0

  for i in range(L-1,len(lst)+1):
    if lst[i-L:i] == comp:
      cnt += 1

  print('#{} {}'.format(T, cnt))