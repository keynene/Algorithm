dx = [1,0,-1]
dy = [0,-1,0]

def dfs(x,y,dx,dy):
  global ans
  nx = x+dx
  ny = y+dy

  if 0<=nx<8 and 0<=ny<8:
    if chess[ny][nx] == '.':
      dfs(nx,ny,dx,dy)
    else:
      ans = 'no'
      return

for T in range(int(input())):
  chess = [list(map(str, input())) for _ in range(8)]
  ans = 'yes'
  cnt = 0

  for y in range(8):
    for x in range(8):
      if chess[y][x] == 'O':
        cnt += 1
        for i in range(3):
          dfs(x,y,dx[i],dy[i])

  if cnt != 8:
    ans = 'no'

  print(f'#{T+1} {ans}')