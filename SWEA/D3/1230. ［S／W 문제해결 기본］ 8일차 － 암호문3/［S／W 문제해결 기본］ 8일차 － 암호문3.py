for T in range(1,11):
  N = int(input())
  secret = list(map(int,input().split()))
  M = int(input())
  command = list(map(str,input().split()))

  for i in range(len(command)):
    if command[i]=='I':
      for j in range(int(command[i+2])):
        secret.insert(int(command[i+1])+j,int(command[i+3+j]))
        
    elif command[i]=='D':
      del secret[int(command[i+1]):int(command[i+1])+int(command[i+2])]

    elif command[i]=='A':
      for j in range(int(command[i+1])):
        secret.append(int(command[i+2+j]))

  print('#{} {} {} {} {} {} {} {} {} {} {}'.format(T,*secret))
