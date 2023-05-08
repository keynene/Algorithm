from collections import deque
from copy import deepcopy

dx = [-1,1]

def bfs(x,y,ladder):
  global res, ans
  queue = deque()
  queue.append((x,y,deepcopy(ladder),0))
  answer = x

  while queue:
    x,y,l,d = queue.popleft()
    isChange = False
    l[y][x] = 0

    if y == 99:
      if res == 0 or res > d:
        res = d
        ans = answer
      return

    for i in range(2):
      cnt = 0
      nx = x+dx[i]

      if 0<=nx<100 and l[y][nx] == 1:
        while 0<=nx<100 and l[y][nx] > 0 :
          l[y][nx] = 0
          nx += dx[i]
          cnt += 1
        nx -= dx[i]
        l[y][nx] = 0
        queue.append((nx,y+1,l,d+cnt+1))
        isChange = True

    if not isChange:  
      queue.append((x,y+1,l,d+1))


for T in range(1,11):
  tc = int(input())
  ladder = [list(map(int,input().split())) for _ in range(100)]

  res = 0
  ans = 0

  for y in range(1):
    for x in range(100):
      if ladder[y][x] == 1:
        bfs(x,y,ladder)
  
  print('#{} {}'.format(T,ans))
