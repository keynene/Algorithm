def is_pal(arr, leng):
    for lst in arr:
        for i in range(N-leng+1):
            for j in range(leng//2):
                if lst[i+j] != lst[i+leng-1-j]:
                    break
            else:
                return True
    return False

for _ in range(1,11):
    t = int(input())
    N = 100
    arr1 = [input() for _ in range(N)]
    arr2 = ["".join(x) for x in zip(*arr1)]

    for leng in range(N,1,-1):
        if is_pal(arr1, leng) or is_pal(arr2, leng):
            break
    print(f'#{t} {leng}')