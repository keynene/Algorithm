from collections import deque

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(num,x,y):
  global cnt, start, next
  queue = deque()
  queue.append((num,x,y,1))
  next = 0

  while queue:
    n,x,y,d = queue.popleft()

    for i in range(4):
      nx = x+dx[i]
      ny = y+dy[i]

      if 0<=nx<N and 0<=ny<N and room[ny][nx] == room[y][x]+1:
        queue.append((n,nx,ny,d+1))

    if cnt < d:
      cnt = d
      start = n
    next = d


for T in range(1, int(input())+1):
  N = int(input())
  room = [list(map(int,input().split())) for _ in range(N)]

  num = 1

  start = 0
  cnt = 0
  next = 0

  while(num <= N*N):
    for y in range(N):
      for x in range(N):
        if room[y][x] == num:
          bfs(num,x,y)
    num += next

  print('#{} {} {}'.format(T,start,cnt))