dx = [1,1,0,-1]
dy = [0,1,1,1]

def dfs(x,y):
  global ans

  for i in range(4):
    nx = x+dx[i]
    ny = y+dy[i]
    cnt = 1

    while 0<=nx<N and 0<=ny<N and arr[ny][nx] == 'o':
      cnt += 1
      nx += dx[i]
      ny += dy[i]

      if cnt >= 5:
        ans = 'YES'
        return

for T in range(int(input())):
  N = int(input())
  arr = [list(map(str, input().rstrip())) for _ in range(N)]
  ans = 'NO'

  for y in range(N):
    for x in range(N):
      if arr[y][x] == 'o':
        dfs(x,y)

  print(f'#{T+1} {ans}')