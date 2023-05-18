for T in range(int(input())):
  N = int(input())
  ans = 0

  for y in range(-N,N+1):
    for x in range(-N,N+1):
      if x**2 + y**2 <= N**2:
        ans += 1
  
  print(f'#{T+1} {ans}')