for TC in range(int(input())):
  S,T = map(str, input().split())
  ans = 'yes'
  fs, ft = '', ''
  mx = len(S)*len(T)

  if S != T:
    while len(fs) < mx:
      fs += S
    while len(ft) < mx:
      ft += T

    if fs != ft:
      ans = 'no'

  print(f'#{TC+1} {ans}')