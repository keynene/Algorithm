from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y,dep,num):
  global res
  queue = deque()
  queue.append((x,y,dep,num))
  
  while queue:
    x,y,dep,num = queue.popleft()

    if dep == 7:
      res.add(num)
      continue;
  
    for i in range(4):
      nx = x+dx[i]
      ny = y+dy[i]
      
      if 0<=nx<4 and 0<=ny<4 :
        queue.append((nx,ny,dep+1,num+amap[ny][nx]))

for T in range(1,int(input())+1):
  amap = [list(map(str, input().split())) for _ in range(4)]
  res = set()
  
  for y in range(4):
    for x in range(4):
      bfs(x,y,1,amap[y][x])

  print('#{} {}'.format(T, len(res)))