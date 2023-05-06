for T in range(1,int(input())+1):
  N, L = map(int, input().split())
  point = [list(map(int, input().split())) for _ in range(N)]
  dp = [[0]*(L+1) for _ in range(N+1)]

  for i in range(1,N+1):
    for j in range(1,L+1):
      if j-point[i-1][1] >= 0:
        dp[i][j] = max(point[i-1][0]+dp[i-1][j-point[i-1][1]],dp[i-1][j])
      else: dp[i][j] = dp[i-1][j]

  print('#{} {}'.format(T,dp[N][L]))