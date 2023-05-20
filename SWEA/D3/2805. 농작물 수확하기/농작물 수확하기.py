for T in range(int(input())):
  N = int(input())
  M = N//2
  graph = [list(map(int, input())) for _ in range(N)]
  ans = 0

  for i in range(N):
    if i <= M:
      for j in range(M-i, M+i+1):
        ans += graph[i][j]
    else:
      for j in range(i-N//2, N-(i-N//2)):
        ans += graph[i][j]

  print(f'#{T+1} {ans}')