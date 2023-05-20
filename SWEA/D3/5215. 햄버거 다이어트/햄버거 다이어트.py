for T in range(int(input())):
  N,L = map(int, input().split())
  ham = [list(map(int,input().split())) for _ in range(N)]
  dp = [[0]*(L+1) for _ in range(N+1)]

  for i in range(1,N+1):
    for j in range(1,L+1):
      if j-ham[i-1][1] >= 0:
        dp[i][j] = max(dp[i-1][j], dp[i-1][j-ham[i-1][1]]+ham[i-1][0])
      else:
        dp[i][j] = dp[i-1][j]

  print(f'#{T+1} {dp[-1][-1]}')