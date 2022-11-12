import sys
input = sys.stdin.readline

N = sorted(list(input().rstrip()), reverse = True)
num = 0
num_str = ''
for i in range(len(N)):
    num += int(N[i])
    num_str += N[i]

if int(num_str)%10 == 0 and num%3 == 0:
    print(num_str)

else:
    print(-1)