import sys
input = sys.stdin.readline

a,b,v = map(int, input().split())

day = (v-b)/(a-b)
if day > int(day):
    print(int(day)+1)
else:
    print(int(day))