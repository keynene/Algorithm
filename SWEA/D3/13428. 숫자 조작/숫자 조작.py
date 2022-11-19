from copy import deepcopy

def dfs(n):
    global maxR, minR
    if n > 0:
        maxR = max(maxR, int("".join(map(str,arr))))
        minR = min(minR, int("".join(map(str,arr))))
        return
    
    for i in range(L):
        for j in range(i+1,L):
            arr[i], arr[j] = arr[j], arr[i]
            if arr[0] != 0:
                chk = int("".join(map(str,arr)))
                if (n,chk) not in v:
                    v.append((n,chk))
                    dfs(n+1)
            arr[i], arr[j] = arr[j], arr[i]


for t in range(int(input())):

    Num = input()
    N = int(Num)  #숫자 12345
    minR = maxR =int(Num)
    L = len(Num)  #종료길이
    arr = list(map(int, str(Num)))
    v = []

    dfs(0)

    print(f'#{t+1} {minR} {maxR}')