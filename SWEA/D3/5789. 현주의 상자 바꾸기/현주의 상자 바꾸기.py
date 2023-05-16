for T in range(1,int(input())+1):
  N,Q = map(int, input().split())
  lst = [0 for _ in range(N+1)]

  for i in range(1,Q+1):
    l, r = map(int, input().split())
    for j in range(l,r+1):
      lst[j] = i
  del lst[0]

  print(f'#{T} ',end="")
  print(*lst)