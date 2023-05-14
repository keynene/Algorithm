from collections import deque

for T in range(1,int(input())+1):
  n,m = map(int,input().split())
  r = [0]+[int(input()) for _ in range(n)]
  w = [0]+[int(input()) for _ in range(m)]
  v = [0]*(n+1)
  lst = [int(input()) for _ in range(2*m)]
  queue,wait = deque(),deque()
  ans = 0

  for num in lst:
    queue.append(num)

  while queue:
    state = queue.popleft()

    if state > 0:
      for i in range(1,n+1):
        if v[i] == 0:
          v[i] = state
          ans += (r[i]*w[state])
          break
      if state not in v:
        wait.append(state)

    else:
      for i in range(1,n+1):
        if v[i] == (-1)*state:
          if wait:
            state = wait.popleft()
            v[i] = state
            ans += (r[i]*w[state])
            break
          else: v[i] = 0

  print(f'#{T} {ans}')