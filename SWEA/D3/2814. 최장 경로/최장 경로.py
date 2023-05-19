def dfs(s,v):
  global ans
  ans = max(ans,len(v))

  for e in graph[s]:
    if e not in v:
      dfs(e,v+[e])


for T in range(int(input())):
  N,M = map(int, input().split())
  graph = [[] for _ in range(N+1)]
  ans = 0

  for _ in range(M):
    u,v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

  for s in range(1,N+1):
    dfs(s,[s])

  print(f'#{T+1} {ans}')