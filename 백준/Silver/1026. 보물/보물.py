N = int(input())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())), key=lambda x:-x)
S = 0

for i in range(N):
    S += A[i]*B[i]
print(S)