import sys
m,n = map(int, sys.stdin.readline().split())

def sosu(num):
    if num == 1: return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False
        return True

for i in range(m, n+1):
    if sosu(i):
        print(i)