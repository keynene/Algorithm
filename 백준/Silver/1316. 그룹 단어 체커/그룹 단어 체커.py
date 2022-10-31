import sys
input = sys.stdin.readline

n = int(input().strip())
word = [input().strip() for _ in range(n)]
cnt = n

for test in word:
    check = {}
    check_len = 0
    check.clear()
    for i in range(len(test)):
        if test[i:i+1] in check:
            if test[i:i+1] == test[i-1:i]:
                check[test[i:i+1]] += 1
                check_len += 1
            else:
                break
        else:
            check[test[i:i+1]] = 1
            check_len += 1
    if check_len != len(test):
        cnt -= 1
        
print(cnt)