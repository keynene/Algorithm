for T in range(int(input())):
  N = int(input())
  ans = 0

  for i in range(1,int(N**(1/2))+1):
    if N%i == 0:
      j = N//i

      if ans == 0:
        ans = i-1+j-1
      else:
        ans = min(ans,i-1+j-1)

  print(f'#{T+1} {ans}')