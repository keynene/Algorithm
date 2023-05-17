for T in range(1, int(input())+1):
  st = list(input().split())
  dp = [[0]*(len(st[1])+1) for _ in range(len(st[0])+1)]

  for i in range(1,len(dp)):
    for j in range(1, len(dp[0])):
      if st[0][i-1] == st[1][j-1]:
        dp[i][j] = dp[i-1][j-1]+1
      else:
        dp[i][j] = max(dp[i-1][j], dp[i][j-1])

  print('#{} {}'.format(T, dp[-1][-1]))