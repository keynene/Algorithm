for T in range(1,int(input())+1):
  N = int(input())
  rec = [list(map(str, input().rstrip())) for _ in range(N)]
  minX, minY = 21,21
  maxX, maxY = 0,0
  ans = 'yes'
  
  for i in range(N):
    for j in range(N):
      if rec[i][j] == '#':
        minX = min(minX, j)
        maxX = max(maxX, j)
        minY = min(minY, i)
        maxY = max(maxY, i)

  for i in range(minY, maxY+1):
    for j in range(minX, maxX+1):
      if rec[i][j] != '#':
        ans = 'no'

  if maxX-minX != maxY-minY:
    ans = 'no'

  print(f'#{T} {ans}')