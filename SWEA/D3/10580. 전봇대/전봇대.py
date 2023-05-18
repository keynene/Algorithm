for T in range(int(input())):
  N = int(input())
  edge = sorted([list(map(int, input().split())) for _ in range(N)])
  ans = 0

  for a,b in edge:
    for c,d in edge:
      if a >= c:
        continue
      elif b > d:
        ans += 1

  print(f'#{T+1} {ans}')