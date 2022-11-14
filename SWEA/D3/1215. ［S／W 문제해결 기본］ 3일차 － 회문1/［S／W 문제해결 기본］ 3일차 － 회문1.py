for t in range(1,11):
    N = int(input())
    M = N//2
    amap = [list(map(str, input().rstrip())) for _ in range(8)]
    comp,compj = [], []
    ans = 0

    for i in range(8):
        for j in range(8):
            if len(comp) < N:
                comp.append(amap[i][j])
            if len(comp) >= N:
                s, e = 0, -1
                cnt = 0
                for _ in range(M):
                    if comp[s] == comp[e]:
                        cnt += 1
                        s += 1
                        e -= 1
                    else:
                        break
                if cnt == M:
                    ans += 1
                del comp[0]
            

            if len(compj) < N:
                compj.append(amap[j][i])
            if len(compj) >= N:
                sj, ej = 0, -1
                cntj = 0
                for _ in range(M):
                    if compj[sj] == compj[ej]:
                        cntj += 1
                        sj += 1
                        ej -= 1
                    else:
                        break
                if cntj == M:
                    ans += 1
                del compj[0]


        comp.clear()
        compj.clear()

    print(f'#{t} {ans}')