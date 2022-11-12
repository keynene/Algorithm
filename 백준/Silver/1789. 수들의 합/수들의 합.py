import sys
input = sys.stdin.readline
num, i = 0, 1
S = int(input())

while True:
    num += i

    if num == S:
        print(i)
        break

    elif num > S:
        print(i-1)
        break
    
    else:
        i += 1