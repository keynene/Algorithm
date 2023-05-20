import sys
from collections import deque
input = sys.stdin.readline

dx = [2,1,-1,-2,-2,-1,1,2]
dy = [1,2,2,1,-1,-2,-2,-1]

def bfs(sx,sy):
  global ans
  if sx==ex and sy==ey:
    return
  queue = deque()
  queue.append((sx,sy))

  while queue:
    x,y = queue.popleft()
    if x==ex and y==ey:
      ans = chess[y][x]
      return

    for i in range(8):
      nx = x+dx[i]
      ny = y+dy[i]

      if 0<=nx<N and 0<=ny<N and chess[ny][nx] == 0:
        chess[ny][nx] = chess[y][x]+1
        queue.append((nx,ny))

for T in range(int(input())):
  N = int(input())
  chess = [[0]*N for _ in range(N)]
  sx,sy = map(int, input().split())
  ex,ey = map(int, input().split())
  ans = 0

  bfs(sx,sy)

  print(ans)
