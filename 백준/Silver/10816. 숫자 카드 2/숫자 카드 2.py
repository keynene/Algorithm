import sys


def bs(arr, target, start, end):
    if start > end:
        return 0
    mid = (start+end)//2
    if arr[mid] == target :
        return cnt.get(target)
    elif arr[mid] > target :
        return bs(arr, target, start, mid-1)
    else:
        return bs(arr, target, mid+1, end)

n = int(sys.stdin.readline().rstrip())
num = sorted(list(map(int, sys.stdin.readline().split())))
m = int(sys.stdin.readline().rstrip())
comp = list(map(int, sys.stdin.readline().split()))

cnt = {}
for i in num :
    if i in cnt :
        cnt[i] += 1
    else :
        cnt[i] = 1

for i in comp :
    print(bs(num, i, 0, len(num)-1), end=' ')