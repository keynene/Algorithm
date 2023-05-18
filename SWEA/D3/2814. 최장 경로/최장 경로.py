from collections import deque

def dfs(i,v):
  global ans
  ans = max(ans, len(v))

  for s, e in edge:
    if i == s and e not in v:
      dfs(e,v+[e])
  

for T in range(int(input())):
  N,M = map(int, input().split())
  edge = [list(map(int, input().split())) for _ in range(M)]
  v = []
  ans = 0

  for x,y in edge:
    if [y,x] not in edge:
      edge.append([y,x])
  edge.sort()

  for i in range(1,N+1):
    dfs(i,v+[i])

  print(f'#{T+1} {ans}')