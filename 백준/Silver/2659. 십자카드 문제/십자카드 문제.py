import sys
from collections import deque
input = sys.stdin.readline

def timeNumber(n):
	global cnt
	global minR

	a,b,c,d = map(int, str(n))
	if 0 in (a,b,c,d):
		minR = 10000
		return

	if cnt == 4 :
		cnt = 0
		return
	
	a,b,c,d = map(str, str(n))
	n = int(str(b+c+d+a))
	minR = min(minR,n)
	cnt += 1
	timeNumber(n)


N = list(map(str, input().split()))
num = "".join(N)
minR = 10000
cnt = 0
timeNumber(num)
comp = minR

count = 1
for i in range(1111,comp):
	timeNumber(i)
	if minR == i : count += 1
	minR = 10000

print(count)