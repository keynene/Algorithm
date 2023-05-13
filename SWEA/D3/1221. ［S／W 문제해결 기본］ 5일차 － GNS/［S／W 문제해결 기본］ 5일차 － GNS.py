strToNum = {"ZRO":0, "ONE":1, "TWO":2, "THR":3, "FOR":4, "FIV":5, "SIX":6, "SVN":7, "EGT":8, "NIN":9}
numToStr = {0:"ZRO", 1:"ONE", 2:"TWO", 3:"THR", 4:"FOR", 5:"FIV", 6:"SIX", 7:"SVN", 8:"EGT", 9:"NIN"}

for T in range(1, int(input())+1):
  no, L = map(str, input().split())
  L = int(L)
  number = list(map(str, input().split()))
  toNum = []

  for i in range(L):
    toNum.append(strToNum.get(number[i]))
  toNum = sorted(toNum)
  number = []

  for i in range(L):
    number.append(numToStr.get(toNum[i]))

  print(f'#{T}')
  print(*number)
