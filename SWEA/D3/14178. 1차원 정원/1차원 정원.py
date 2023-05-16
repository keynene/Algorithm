for T in range(1, int(input())+1):
  N, D = map(int, input().split())
  if N%(1+2*D) == 0:
    ans = N//(1+2*D)
  else: ans = N//(1+2*D)+1

  print(f'#{T} {ans}')