from copy import deepcopy
al = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def dfs(n,v,now):
  global ans, res
  v = deepcopy(v)

  if len(v) >= 26:
    ok = 0
    for a in al:
      if a in v:
        ok += 1
      else : break
    if ok == 26:
      if now not in res:
        ans += 1
        res.append(now)

  if n >= N:
    return
  
  
  dfs(n+1,v,now)

  for wds in word[n]:
    if wds not in v:
      v.append(wds)

  dfs(n+1,v,now+[n])

for TC in range(int(input())):
  N = int(input())
  word = [input().rstrip() for _ in range(N)]
  ans = 0
  res = []

  dfs(0,[],[])

  
  print(f'#{TC+1} {ans}')