import sys
X = int(input())
plus = 0
for i in range(int(input())):
    a,b = map(int,sys.stdin.readline().split())
    plus = plus+a*b
print('Yes' if X==plus else 'No');