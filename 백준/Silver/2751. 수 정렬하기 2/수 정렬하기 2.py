N = int(input());
num = [int(input()) for _ in range(N)]
sort_num = list(sorted(num))
for i in range(len(num)):
    print(sort_num[i])