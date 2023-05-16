for T in range(1,int(input())+1):
  lst = list(map(int, input().split()))
  ans = 0

  for num in lst:
    if lst.count(num) == 1:
      ans = num
      break
  
  if ans == 0:
    ans = lst[0]

  print(f'#{T} {ans}')