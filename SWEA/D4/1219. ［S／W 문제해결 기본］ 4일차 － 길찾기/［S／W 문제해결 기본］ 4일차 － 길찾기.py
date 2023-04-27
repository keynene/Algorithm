from copy import deepcopy
from collections import deque

def bfs(srt, visited):
  global ans
  vis = deepcopy(visited)
  queue = deque()

  queue.append((srt,vis))
  
  while queue:
    s, v = queue.popleft()

    if s == 99:
      ans = 1
    
    for start, end in graph:
      if s == start and not v[s]:
        v[s] = True
        queue.append((end,v))
        v[s] = False
      if start > s: break;


for T in range(1, 11):
  tc, e = map(int,input().split())
  edge = list(map(int, input().split()))
  graph = []
  visited = [False]*100
  ans = 0


  for i in range(1,len(edge),2):
    graph.append([edge[i-1],edge[i]])
  graph.sort()
  
  bfs(graph[0][0], visited)

  print('#{} {}'.format(T, ans))