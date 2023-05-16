for T in range(1,int(input())+1):
  word = input().rstrip()
  ans = ''
  
  for al in word:
    if al not in ('a','e','i','o','u'):
      ans += al

  print(f'#{T} {ans}')