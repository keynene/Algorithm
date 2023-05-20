for T in range(int(input())):
  N = int(input())
  ans = 0
  for a in range(1,int(N**(1/2))+1):
    if N%a == 0:
      b = N//a
      if ans != 0:
        ans = min(ans,a-1+b-1)
      else:
        ans = a-1+b-1

  print(f'#{T+1} {ans}')