def dfs(n):
    global maxR, minR
    if n == 1:
        maxR = max(maxR, int("".join(map(str,arr))))
        minR = min(minR, int("".join(map(str,arr))))
        return

    for i in range(L-1):
        for j in range(i+1,L):
            arr[i], arr[j] = arr[j], arr[i]
            if arr[0] == 0:
                arr[i], arr[j] = arr[j], arr[i]
                continue

            chk = int("".join(map(str,arr)))
            if (n, chk) not in V:
                dfs(n+1)
                V.append((n,chk))

            arr[i], arr[j] = arr[j], arr[i]

for t in range(int(input())):
    maxR = int(input())
    minR = maxR
    arr = list(map(int, str(maxR)))
    L = len(arr)
    V = []

    dfs(0)

    print(f'#{t+1} {minR} {maxR}')