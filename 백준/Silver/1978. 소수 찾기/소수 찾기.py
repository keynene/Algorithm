import sys
input = sys.stdin.readline

n = int(input().strip())
number = list(map(int,input().split()))

cnt = 0
for num in number:
    err = 0
    if num > 1:
        for j in range(2,num):
            if num % j == 0:
                err += 1
        if err == 0:
            cnt += 1
print(cnt)
