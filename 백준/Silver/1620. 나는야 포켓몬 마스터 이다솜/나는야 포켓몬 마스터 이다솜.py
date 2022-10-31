from ast import Num
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
pok_name = {}
pok_num = {}

for i in range(1,n+1):
    name = input().rstrip()
    pok_name[i] = name
    pok_num[name] = i

test = [input().rstrip() for _ in range(m)]
for i in test:
    if i.isdigit():
        print(pok_name[int(i)])
    else:
        print(pok_num[i])
