for T in range(1,int(input())+1):
  dD, dH, dM = 11, 11, 11
  D, H, M = map(int, input().split())
  ans = -1

  aD = D-dD
  aH = H-dH
  aM = M-dM

  if aD >= 0:
    if aH >= 0:
      if aM >= 0:
        ans = aD*24*60 + aH*60 + aM
      else:
        ans = aD*24*60 + (aH-1)*60 + aM+60
    else:
      if aM >= 0:
        ans = (aD-1)*24*60 + (aH+24)*60 + aM
      else:
        ans = (aD-1)*24*60 + (aH+24-1)*60 + aM+60

  if ans < 0 :
    ans = -1


  print(f'#{T} {ans}')