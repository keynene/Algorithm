for TC in range(int(input())):
  S,T = map(str, input().split())
  sl, tl = len(S), len(T)
  ans = 'yes'

  if S*tl != T*sl:
    ans = 'no'
  print(f'#{TC+1} {ans}')