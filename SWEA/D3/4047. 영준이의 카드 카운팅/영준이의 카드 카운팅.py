for T in range(1,int(input())+1):
  S = input().rstrip()
  L = len(S)
  err = False
  ans = [13, 13, 13, 13]

  for i in range(3,L+1,3):
    for j in range(i+3,L+1,3):
      if S[i-3:i] == S[j-3:j]:
        err = True

    if err:
      break

    else:
      if S[i-3] == 'S':
        ans[0] -= 1
      elif S[i-3] == 'D':
        ans[1] -= 1
      elif S[i-3] == 'H':
        ans[2] -= 1
      elif S[i-3] == 'C':
        ans[3] -= 1

  if err:
    print('#{} ERROR'.format(T))
  else:
   print('#{} {} {} {} {}'.format(T, *ans))


