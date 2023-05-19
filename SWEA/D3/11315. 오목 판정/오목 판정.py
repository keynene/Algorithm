dx = [1,1,0,-1]
dy = [0,-1,-1,-1]

def dfs(x,y,dx,dy,d):
  global ans
  if d >= 5:
    ans = 'YES'
    return
  
  else:
    nx = x+dx
    ny = y+dy
    if 0<=nx<N and 0<=ny<N and arr[ny][nx] == 'o':
      dfs(nx,ny,dx,dy,d+1)
  


for T in range(int(input())):
  N = int(input())
  arr = [list(map(str,input())) for _ in range(N)]
  ans = 'NO'

  for y in range(N):
    for x in range(N):
      if arr[y][x] == 'o':
        for i in range(4):
          nx = x+dx[i]
          ny = y+dy[i]
          if 0<=nx<N and 0<=ny<N and arr[ny][nx] == 'o':
            dfs(nx,ny,dx[i],dy[i],2)

    if ans == 'YES':
      break

  print(f'#{T+1} {ans}')