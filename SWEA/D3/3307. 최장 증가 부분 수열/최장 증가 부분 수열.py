for T in range(int(input())):
  N = int(input())
  lst = [0]+list(map(int, input().split()))
  dp = [0]*(N+1)

  for i in range(1,N+1):
    mx = 0
    for j in range(i):
      if lst[i] > lst[j]:
        mx = max(mx, dp[j])
    dp[i] = mx+1

  print(f'#{T+1} {max(dp)}')
