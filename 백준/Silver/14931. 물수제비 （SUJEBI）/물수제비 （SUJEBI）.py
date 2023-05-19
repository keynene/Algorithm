L = int(input())
score = [0]+list(map(int, input().split()))
ans = []
d=1

while d <= L:
  res = 0
  for i in range(d,L+1,d):
    res += score[i]
  ans.append([d, res])
  d += 1


ans = sorted(ans, key=lambda x:-x[1])

if ans[0][1] <= 0:
  ans[0][0], ans[0][1] = 0,0
print(*ans[0])