import sys
input = sys.stdin.readline

n,k = map(int, input().split())
coin = sorted([int(input().rstrip()) for _ in range(n)], key=lambda x:-x)

cnt = 0

for money in coin:
    cnt += k//money
    k %= money
print(cnt)