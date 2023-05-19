for T in range(int(input())):
  N,M,K = map(int, input().split())
  lst = sorted(list(map(int, input().split())))
  ans = 'Possible'

  if lst[0] == 0:
    ans = 'Impossible'
    print(f'#{T+1} {ans}')
  else:
    for i in range(N):
      if (lst[i]//M)*K-(i+1) < 0:
        ans = 'Impossible'
        break
    print(f'#{T+1} {ans}')
