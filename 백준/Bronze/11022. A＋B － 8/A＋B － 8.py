import sys
for i in range(int(input())):
    a,b = sys.stdin.readline().split()
    print('Case #',i+1,': ',a,' + ',b,' = ',int(a)+int(b),sep='')