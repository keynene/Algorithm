import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
sum_arr = sum(arr)
ans = 0

for i in arr:
    sum_arr  -= i
    ans += i*(sum_arr)
    
print(ans)