for T in range(int(input())):
  N = int(input())
  lst = sorted(list(map(int, str(N))))
  ans = 'impossible'
  i = 2
  
  while len(str(i*N)) <= len(lst):
    num = sorted(list(map(int, str(i*N))))
    if lst == num:
      ans = 'possible'
      break
    i += 1

  print(f'#{T+1} {ans}')