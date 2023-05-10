dx = [1,1,0,-1,-1,-1,0,1]
dy = [0,1,1,1,0,-1,-1,-1]

for T in range(1,int(input())+1):
  N, M = map(int, input().split())
  graph = [[0]*(N) for _ in range(N)]
  graph[N//2-1][N//2-1] = 2
  graph[N//2][N//2-1] = 1
  graph[N//2-1][N//2] = 1
  graph[N//2][N//2] = 2
  move = [list(map(int, input().split())) for _ in range(M)]

  for x, y, mode in move:
    x,y = x-1,y-1
    graph[y][x] = mode

    for i in range(8):
      d = 0
      going = True
      nx = x+dx[i]
      ny = y+dy[i]

      if 0<=nx<N and 0<=ny<N and graph[ny][nx]!=0 and graph[ny][nx]!=mode:
        while going:
          nx += dx[i]
          ny += dy[i]
          d += 1
          
          if 0<=nx<N and 0<=ny<N:
            if graph[ny][nx] == mode:
              while d:
                graph[ny-dy[i]*d][nx-dx[i]*d] = mode
                d -= 1
              going = False
            if graph[ny][nx] == 0:
              going = False
          else: going = False

  bcnt, wcnt = 0,0
  for x in graph:
    bcnt += x.count(1) 
    wcnt += x.count(2) 


  print('#{} {} {}'.format(T,bcnt,wcnt))