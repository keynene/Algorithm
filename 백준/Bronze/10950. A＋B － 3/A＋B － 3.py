T = int(input())
C = [0]*T
for i in range(T):
    C[i] = sum(map(int,input().split()))
for i in range(T):
    print(C[i])