import sys
arr = [0]*9
max = 0;
cnt = 0;
for i in range(9):
    arr[i] = int(input())
    if arr[i] >= max:
        max = arr[i]
        cnt = i+1
    else:
        continue;

print(max, cnt, sep="\n")