for T in range(1,int(input())+1):
  N = int(input())
  lst = list(map(int,input().split()))
  ans = 0

  for i in range(N):
    for j in range(i+1,N):
      danzo = True
      if i != j:
        temp = list(map(int, str(lst[i]*lst[j])))

        if len(temp) > 1:
          for k in range(1,len(temp)):
            if temp[k-1] > temp[k]:
              danzo = False
              break

      if danzo:
        ans = max(ans, lst[i]*lst[j])

  if ans == 0:
    ans = -1
  print(f'#{T} {ans}')