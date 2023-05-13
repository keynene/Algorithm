from collections import deque
from copy import deepcopy

def dfs(c, v):
  global cnt
  cnt = max(cnt, len(v))

  for n in graph[c]:
    if n not in v:
      dfs(n, v+[n])

for T in range(1,int(input())+1):
  N, M = map(int, input().split())
  graph = [[] for _ in range(N+1)]
  cnt = 0

  for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

  for s in range(1,N+1):
    dfs(s, [s])

  print(f'#{T} {cnt}')