import sys

n = int(sys.stdin.readline().strip())
num = set(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline().strip())
comp = list(map(int, sys.stdin.readline().split()))

result = []
for i in comp :
    if i in num :
        result.append(1)
    else:
        result.append(0)
for i in result:
    print(i, end=' ')