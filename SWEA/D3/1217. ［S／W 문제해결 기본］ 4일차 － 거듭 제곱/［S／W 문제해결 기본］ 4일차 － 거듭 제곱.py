def  mul(num,n):
    global cnt, ans
    if n == cnt+1:
        return
    ans *= num
    mul(num,n+1)

for _ in range(10):
    t = int(input())
    ans = 1
    N, cnt = map(int,input().split())

    mul(N, 1)

    print(f'#{t} {ans}')