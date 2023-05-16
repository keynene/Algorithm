for T in range(1, int(input())+1):
  N, K = map(int, input().split())
  score = sorted(list(map(int, input().split())), reverse=True)

  print(f'#{T} {sum(score[:K])}')