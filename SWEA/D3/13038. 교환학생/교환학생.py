from collections import deque

for T in range(1,int(input())+1):
  N = int(input())
  week = list(map(int, input().split()))
  ans = 0
  s = 0
  queue = deque()

  for i in range(7):
    if week[i] == 1:
      queue.append(i)

  while queue:
    n = N
    s = queue.popleft()
    cnt = 0

    while n>0:
      for i in range(s,7):
        cnt += 1
        if week[i] == 1:
          n -= 1
          if n == 0:
            break
      if n != 0:
        s = 0

    if ans == 0:
      ans = cnt
    else:
      ans = min(ans, cnt)

  print(f'#{T} {ans}')