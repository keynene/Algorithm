import sys
input = sys.stdin.readline

s = input().rstrip()
comp = set()

for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        comp.add(s[i:j])
print(len(comp))