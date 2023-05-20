def dfs(n,v):
  global ans
  ans = max(ans, len(v))

  for j in graph[n]:
    if j not in v:
      dfs(j,v+[j])

for T in range(int(input())):
  N,M = map(int,input().split())
  edge = [list(map(int,input().split())) for _ in range(M)]
  graph = [[] for _ in range(N+1)]
  ans = 0

  for u,v in edge:
    graph[u].append(v)
    graph[v].append(u)

  for i in range(1,N+1):
    dfs(i,[i])

  print(f'#{T+1} {ans}')