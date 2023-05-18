for T in range(int(input())):
  N = int(input())
  m = N//2
  arr = [list(map(int, input())) for _ in range(N)]
  ans = 0

  for i in range(N):
    if i <= m:
      for j in range(m-i, m+i+1):
        ans += arr[i][j]
    else:
      for j in range(i-m,N-(i-m)):
        ans += arr[i][j]
  print(f'#{T+1} {ans}')