for T in range(1,int(input())+1):
  L,U,X = map(int, input().split())
  ans = 0

  if X > U:
    ans = -1
  elif X < L:
    ans = L-X

  print(f'#{T} {ans}')