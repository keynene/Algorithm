for T in range(1,int(input())+1):
  ans = 0
  for i in range(int(input())):
    a,b = map(float, input().split())
    ans += a*b*10000

  print('#{} {:.6f}'.format(T, ans/10000))