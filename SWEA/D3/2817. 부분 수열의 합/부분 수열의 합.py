def dfs(n,sm):
  global cnt
  if n == N:
    if sm == K:
      cnt += 1
    return
  
  dfs(n+1,sm+num[n])
  dfs(n+1,sm)

for T in range(int(input())):
  N, K = map(int, input().split())
  num = list(map(int,input().split()))
  cnt = 0

  dfs(0,0)

  print(f'#{T+1} {cnt}')