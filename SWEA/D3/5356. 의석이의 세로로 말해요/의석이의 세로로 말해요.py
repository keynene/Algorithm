for T in range(1,int(input())+1):
  words = [list(map(str,input())) for _ in range(5)]
  L = 0
  for word in words:
    L = max(L, len(word))
  answer = [[] for _ in range(L)]

  for word in words:
    for i in range(len(word)):
      answer[i].append(word[i])

  print(f'#{T} ',end="")
  for ans in answer:
    print(*ans,end="",sep="")
  print()