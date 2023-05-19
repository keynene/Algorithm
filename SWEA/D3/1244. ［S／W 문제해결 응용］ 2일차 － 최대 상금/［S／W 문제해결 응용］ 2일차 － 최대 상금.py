def dfs(n,v):
  global ans
  if n == cnt:
    ans = max(ans,int("".join(map(str,arr))))
    return
  
  for i in range(L-1):
    for j in range(i+1,L):
      arr[i], arr[j] = arr[j], arr[i]
      chk = int("".join(map(str,arr)))
      if (n,chk) not in v and arr[0] != 0:
        v.append((n,chk))
        dfs(n+1,v)
      arr[i], arr[j] = arr[j], arr[i]
      

for T in range(int(input())):
  num, cnt = map(int, input().split())
  arr = list(map(int, str(num)))
  L = len(arr)
  ans = 0

  dfs(0,[])

  print(f'#{T+1} {ans}')