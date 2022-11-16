def dfs(n):
    global ans
    if n == N:
        ans = max(ans, int("".join(map(str,lst))))
        return
    
    for i in range(L-1):
        for j in range(i+1, L):
            lst[i], lst[j] = lst[j], lst[i]

            chk = int("".join(map(str,lst)))
            if (n, chk) not in V:
                dfs(n+1)
                V.append((n,chk))

            lst[i], lst[j] = lst[j], lst[i]

for tc in range(int(input())):
    st, t = input().split()
    N = int(t)
    lst = []
    for ch in st:
        lst.append(int(ch))
    L = len(lst)
    ans = 0
    V = []
    dfs(0)
    print(f'#{tc+1} {ans}')