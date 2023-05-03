for T in range(1,11):
  N = int(input())
  arr = list(map(int, input().split()))
  C = int(input())
  temp = list(map(str, input().split("I ")))
  del temp[0]
  com = []
  for lst in temp:
    com.append(list(map(int, lst.split())))

  for comlst in com:
    temp = 0
    for j in range(2,len(comlst)):
      arr.insert(comlst[0]+temp,comlst[j])
      temp += 1

  print('#{} {} {} {} {} {} {} {} {} {} {}'.format(T,*arr))