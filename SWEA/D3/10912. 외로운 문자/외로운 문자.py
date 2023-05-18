for T in range(int(input())):
  lst = list(map(str,input().rstrip()))
  roof = True
  ans = 'Good'

  while roof:
    roof = False
    for i in range(len(lst)-1):
      for j in range(i+1,len(lst)):
        if lst[i] == lst[j]:
          del lst[i]
          del lst[j-1]
          roof = True
          break
      if roof: break

  if lst != []:
    ans = ''
    lst.sort()
    for al in lst:
      ans += al

  print(f'#{T+1} {ans}')