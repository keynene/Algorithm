import sys
A = [0]*10
C = [0]*10
for i in range(10):
    A = int(input())
    C[i] = A % 42
C = set(C)
print(len(C))