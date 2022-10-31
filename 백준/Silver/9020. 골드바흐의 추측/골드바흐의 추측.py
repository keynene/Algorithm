import sys
input = sys.stdin.readline

t = int(input().rstrip())

def prime(n):
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

for _ in range(t):
    n = int(input().rstrip())
    a,b = n//2, n//2
    while a > 0:
        if prime(a) and prime(b):
            print(a, b)
            break
        else:
            a -= 1
            b += 1