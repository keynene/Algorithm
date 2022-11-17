for t in range(int(input())):
    arr = list(map(int, input().split()))
    L = len(arr)
    ans = []

    for i in range(L-2):
        for j in range(i+1, L-1):
            for k in range(j+1, L):
                sumR = arr[i]+arr[j]+arr[k]
                if sumR not in ans:
                    ans.append(sumR)
    ans.sort(reverse = True)

    print(f'#{t+1} {ans[4]}')