for T in range(int(input())):
  lst = input().rstrip()
  ans = 0

  for i in range(len(lst)):
    if lst[i] == '(':
      if i == len(lst)-1:
        ans += 1
      elif lst[i+1] == ')' or '|':
        ans += 1
    if lst[i] == ')':
      if i == 0:
        ans += 1
      elif lst[i-1] == '|':
        ans += 1

  print(f'#{T+1} {ans}')