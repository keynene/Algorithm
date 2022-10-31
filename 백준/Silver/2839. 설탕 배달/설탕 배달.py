import sys
input = sys.stdin.readline

kg = int(input().strip())
rice_j = {0:0, 1:2, 2:4, 3:1, 4:3}
rice_i = {0:0, 1:-1, 2:-2, 3:0, 4:-1}

i = kg//5
j = kg-(5*(kg//5))

if kg == 4 or kg==7:
    print(-1)

elif kg%5 == 0:
    print(i)

else: 
    cnt = i + rice_i.get(j) + rice_j.get(j)
    print(cnt)