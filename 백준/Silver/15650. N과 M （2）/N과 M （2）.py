import sys
input = sys.stdin.readline

n,m = map(int, input().split())
num = []

def bt():
    if len(num) == m:
        print(*num)
        return
    for i in range(1,n+1):
        if len(num)==0 or i > num[-1]:
            if i not in num:
                num.append(i)
                bt()
                num.pop()
bt()