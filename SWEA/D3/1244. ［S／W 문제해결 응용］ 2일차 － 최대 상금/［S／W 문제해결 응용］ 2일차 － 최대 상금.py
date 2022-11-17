def dfs(n):
    global ans
    if n == N:
        ans = max(ans, int("".join(map(str,arr))))
        return
    
    for i in range(L-1):
        for j in range(i+1,L):
            arr[i], arr[j] = arr[j], arr[i]

            chk = int("".join(map(str,arr)))
            if (n, chk) not in V:
                dfs(n+1)
                V.append((n,chk))

            arr[i], arr[j] = arr[j], arr[i]

for t in range(int(input())):
    Num, N = map(str,input().split())
    N = int(N)
    arr = []
    V = []
    for i in Num:
        arr.append(int(i))
    L = len(arr)
    ans = 0

    dfs(0)

    print(f'#{t+1} {ans}')