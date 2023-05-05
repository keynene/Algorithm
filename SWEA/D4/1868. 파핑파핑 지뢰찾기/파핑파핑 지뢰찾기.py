from collections import deque

dx = [1,1,0,-1,-1,-1,0,1]
dy = [0,1,1,1,0,-1,-1,-1]

def numbering(x,y):
  cnt = 0
  for i in range(8):
    nx = x+dx[i]
    ny = y+dy[i]

    if 0<=nx<N and 0<=ny<N and graph[ny][nx] == '*':
      cnt += 1
  return cnt

def star(x,y):
  queue = deque()
  queue.append((x,y))
  graph[y][x] = '*'

  while queue:
    x,y = queue.popleft()

    for i in range(8):
      nx = x+dx[i]
      ny = y+dy[i]

      if 0<=nx<N and 0<=ny<N:
        if graph[ny][nx] != '0':
          graph[ny][nx] = '*'
        else : 
          queue.append((nx,ny))
          graph[ny][nx] = '*'

for T in range(1, int(input())+1):
  N = int(input())
  graph = [list(map(str, input().rstrip())) for _ in range(N)]
  click = 0

  for y in range(N):
    for x in range(N):
      if graph[y][x] == '.':
        graph[y][x] = str(numbering(x,y))

  for y in range(N):
    for x in range(N):
      if graph[y][x] == '0':
        star(x,y)
        click += 1
  
  for y in range(N):
    for x in range(N):
      if graph[y][x] != '*':
        click += 1

  print('#{} {}'.format(T, click))  