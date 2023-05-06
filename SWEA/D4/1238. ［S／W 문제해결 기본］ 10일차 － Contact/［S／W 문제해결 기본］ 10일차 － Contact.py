from collections import deque
from copy import deepcopy

def bfs(S, visited):
  global cnt
  res = 0
  v = deepcopy(visited)
  v[S] = True
  queue = deque()
  queue.append((S,v,0))

  while queue:
    s,v,d = queue.popleft()

    for start, end in callBook:
      if start == s and not v[end]:
        v[end] = True
        queue.append((end,v,d+1))

    if cnt < d:
      cnt = d
      res = s
    elif cnt == d:
      res = max(res,s)
  return res



for T in range(1,11):
  L, S = map(int, input().split())
  lstFromTo = list(map(int, input().split()))
  callBook = []
  visited = [False]*101
  cnt = 0

  for i in range(1, len(lstFromTo)+1,2):
    callBook.append([lstFromTo[i-1], lstFromTo[i]])
  callBook.sort()

  ans = bfs(S, visited)

  print('#{} {}'.format(T, ans))