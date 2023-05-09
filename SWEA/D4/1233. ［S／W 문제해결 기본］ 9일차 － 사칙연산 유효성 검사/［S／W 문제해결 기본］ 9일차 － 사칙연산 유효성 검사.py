for T in range(1,11):
  N = int(input())
  node = [list(map(str, input().split())) for _ in range(N)]
  ans = 1


  if N%2 == 0:
    ans = 0
  else:
    for i in range((N//2)+1,N):
      if node[i][1] == '+' or node[i][1] == '-' or node[i][1] == '*' or node[i][1] == '/':
        ans = 0
        break

  print('#{} {}'.format(T, ans))

