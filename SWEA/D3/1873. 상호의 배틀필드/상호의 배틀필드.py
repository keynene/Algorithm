for T in range(1,int(input())+1):
  H, W = map(int, input().split())
  amap = [list(map(str, input())) for _ in range(H)]
  N = int(input())
  command = input().rstrip()
  nx, ny = 0,0

  for y in range(H):
    for x in range(W):
      if amap[y][x] == '^' or amap[y][x] == 'v' or amap[y][x] == '<' or amap[y][x] == '>':
        nx, ny = x, y

  for i in command:
    if i == 'U':
      if 0<=ny-1 and amap[ny-1][nx] == '.':
        amap[ny][nx] = '.'
        amap[ny-1][nx] = '^'
        ny -= 1
      else:
        amap[ny][nx] = '^'

    if i == 'D':
      if ny+1<H and amap[ny+1][nx] == '.':
        amap[ny][nx] = '.'
        amap[ny+1][nx] = 'v'
        ny += 1
      else:
        amap[ny][nx] = 'v'

    if i == 'L':
      if 0<=nx-1 and amap[ny][nx-1] == '.':
        amap[ny][nx] = '.'
        amap[ny][nx-1] = '<'
        nx -= 1
      else:
        amap[ny][nx] = '<'

    if i == 'R':
      if nx+1<W and amap[ny][nx+1] == '.':
        amap[ny][nx] = '.'
        amap[ny][nx+1] = '>'
        nx += 1
      else:
        amap[ny][nx] = '>'
    
    if i == 'S':
      dx,dy = 0,0
      if amap[ny][nx] == '^': dy = -1
      elif amap[ny][nx] == 'v': dy = +1
      elif amap[ny][nx] == '<': dx = -1
      elif amap[ny][nx] == '>': dx = +1

      shooting = True

      x = nx
      y = ny

      while shooting:
        x += dx
        y += dy
        if 0<=x<W and 0<=y<H:
          if amap[y][x] == '*':
            amap[y][x] = '.'
            shooting = False

          elif amap[y][x] == '#': 
            shooting = False
        
        else : 
          dx, dy = 0,0
          shooting = False
  print('#',T,' ',end="",sep="")
  for i in amap:
    print(*i, sep="")