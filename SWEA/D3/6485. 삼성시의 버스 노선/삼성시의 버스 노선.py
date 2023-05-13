for T in range(1,int(input())+1):
  N = int(input())
  line = [list(map(int, input().split())) for _ in range(N)]
  P = int(input())
  ans = []

  for i in range(P):
    comp = int(input())
    cnt = 0
    for lst in line:
      if comp>=lst[0] and comp<=lst[1]:
        cnt += 1
    ans.append(cnt)

  print("#",T," ",sep="",end="")
  print(*ans)