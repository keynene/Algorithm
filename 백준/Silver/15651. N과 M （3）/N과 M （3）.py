import sys
input = sys.stdin.readline

n,m = map(int, input().split())
num = []

def bt():
    if len(num) == m:
        print(*num)
        return
    for i in range(1,n+1):
        num.append(i)
        bt()
        num.pop()
bt()