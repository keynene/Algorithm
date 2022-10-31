import sys

n = list(map(int,str(input())))
n.sort(key=lambda x:-x)
for i in n:
    print(i,end='')