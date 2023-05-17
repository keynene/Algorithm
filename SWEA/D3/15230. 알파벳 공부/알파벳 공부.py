az = 'abcdefghijklmnopqrstuvwxyz'

for T in range(1,int(input())+1):
  al = input().rstrip()
  cnt = 0

  for i in range(len(al)):
    if al[i] == az[i]:
      cnt += 1
    else: break

  print(f'#{T} {cnt}')