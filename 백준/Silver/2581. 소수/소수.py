import sys
input = sys.stdin.readline

m = int(input().rstrip())
n = int(input().rstrip())
number = [i for i in range(m,n+1)]

sosu = []
for num in number:
    err = 0
    if num > 1:
        for i in range(2,num):
            if num % i == 0:
                err += 1
        if err == 0:
            sosu.append(num)
if len(sosu) == 0:
    print(-1)
else:
    print(sum(sosu),sosu[0], sep="\n")