# [Silver II] 연결 요소의 개수 - 11724 

[문제 링크](https://www.acmicpc.net/problem/11724) 

### 성능 요약

메모리: 204928 KB, 시간: 440 ms

### 분류

그래프 이론(graphs), 그래프 탐색(graph_traversal), 너비 우선 탐색(bfs), 깊이 우선 탐색(dfs)

### 문제 설명

<p>방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2) 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. (1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.</p>

### 출력 

 <p>첫째 줄에 연결 요소의 개수를 출력한다.</p>

## 📖[Python/파이썬] [🥈2] 백준 알고리즘 11724 - 연결 요소의 개수
### 📜문제
![](https://velog.velcdn.com/images/keynene/post/40842c01-6b11-409a-8b5b-af2decd8048e/image.png)
![](https://velog.velcdn.com/images/keynene/post/44c3dc09-8c9b-458c-bcba-8d8fc96717f0/image.png)
![](https://velog.velcdn.com/images/keynene/post/d012f1ad-0709-4266-8cab-7eb75b2b2947/image.png)

* * *


#### DFS(깊이우선탐색)
![](https://velog.velcdn.com/images/keynene/post/bccb3a9b-be02-48d3-8ae1-90bedfa53f2d/image.png)
- 임의의 한 노드에서 시작해서 다음 분기로 넘어가기 전에 해당 분기를 완벽하게 탐색하는 방법
- 자기 자신을 호출하는 재귀/순환 알고리즘의 형태임
- 노드 방문 여부를 검사해놔야 무한루프에 빠질 위험이 줄어듦
- 주로 백트래킹과 함께 쓰여, 모든 노드를 다 방문하는 것을 차단함

* * *

### 📕풀이방향
**"연결 요소의 개수" 라는 말이 애매해서 검색해보니, 만들어지는 "그래프의 개수"였다**

우선 모든 노드를 map으로 만들고, visited 방문검사list를 0으로 초기화하자
dfs(idx)로 방문 여부를 검사하여, 방문하면 visited[idx]를 1로 고쳐주면서 idx가 증가할 때마다 카운팅(cnt+1) 해주자
재귀적으로 map에 있는 모든 노드를 방문했을 때 cnt를 반환하자

* * *

### 📝알고리즘 구현순서
1. n,m과 node를 입력받으면서 amap에 map형태로 저장하자
2. visited list를 0으로 초기화하고 ```dfs()```함수를 만들고,
   ```for loof```를 1~n+1까지 증가시키며 ```visited[i] == 0```일 때 ```dfs()```를 
   호출하자 (```for loof```idx 증가할 때마다 카운팅)

* * *

### 💻결과코드
```python
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
node = [list(map(int, input().split())) for _ in range(m)]
amap = [[] for _ in range(n+1)]

#amap에 그래프 형식으로 넣기
for u,v in node:
    amap[u].append(v)
    amap[v].append(u)

cnt = 0
visited = [0]*(n+1)
def dfs(v):
    visited[v] = 1
    for i in amap[v]:
        if not visited[i]:
            dfs(i)

for i in range(1, n+1):
    #visited[i] == 0일때만 dfs(i)실행
    if not visited[i]:
        dfs(i)
        cnt += 1

print(cnt)
```

* * *

#### ✏️1. n, m, node 입력받으면서 amap 저장
```python
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
node = [list(map(int, input().split())) for _ in range(m)]
amap = [[] for _ in range(n+1)]

for u,v in node:  #node의 [u, v]
    amap[u].append(v)  #node[u]에 v저장
    amap[v].append(u)  #node[v]에 u저장
```

**❓amap 저장 원리**
```
ex. 입력값이 1 2, 2 5 인 경우

- node에 입력받으면서 저장되는 형태
  node[0] = [1, 2]
  node[1] = [2, 5]
  ※node = [[1, 2], [2, 5]]
  
- for loof에서 amap에 저장되는 형태
  1. i == 0:
    amap[1].append(2)
    amap[2].append(1)
  2. i == 1:
    amap[2].append(5)
    amap[5].append(2)
    
  ※amap[1] = 2
    amap[2] = 1, 5
    amap[5] = 2
```
❗ 입력값이 **u → v** 형태로만 들어오니까, **u ↔ v**형태로 저장해준다고 생각하면 편함 
❗❗ DFS, BFS 문제 다룰 때 자주 사용되니 기억해두자
  (쌍방향 인덱싱 == 그래프)


* * *

#### ✏️2. dfs()함수 구현과 for loof에서 호출
```python
cnt = 0  #연결요소 개수 저장
visited = [0]*(n+1)  #방문여부 검사

def dfs(v):
    visited[v] = 1
    for i in amap[v]:
        if not visited[i]:
            dfs(i)

for i in range(1, n+1):
    if not visited[i]:
        dfs(i)
        cnt += 1

print(cnt)
```

❓위 예제에서 DFS 동작원리
```
visited = [0,0,0,0,0,0,0] 
(visited를 n+1하는 이유 : 그래프 인덱싱을 1~n까지로 해줬으므로,
 사실상 visited[0]값은 쓰지 않는다.)

1. for loof으로 i를 증가시키면서 그래프(amap)의 인덱스가 i일 때,
   visited[i]로 인해 i번째 노드를 방문했는지 확인한다.
2. 방문하지 않았으면, dfs(i)를 호출하여 visited[i] = 1 저장하고,
   i인덱스의 노드를 모두 검사한다.
```
![](https://velog.velcdn.com/images/keynene/post/4b412afd-ecc7-4a02-88fd-b192a494d455/image.png)
**잘 모르겠으니, 예제 1를 예로 들어보자**
```python
   #amap[1] = 2, 5
   #amap[2] = 1, 5
   #visited = [0, 0, 0, 0, 0, 0, 0]인 상황
   
   for 1 in range(1, n+1):
     if not visited[1]:  #visited[1] == 0이므로 True
       dfs(1)   #dfs(1)호출
       cnt += 1   #이건 for i가 1인 상황이 종료되면 실행된다!!
       
   #dfs(1)동작
   def dfs(1):
     visited[1] = 1   #visited = [0, 1, 0, 0, 0, 0, 0]이 됨
     for i in amap[1]:   #amap[1]인 2, 5를 하나씩 검사
       if not visited[2]:   # visited[2] = 0이므로 True
         dfs(2)   #dfs(2)호출
         
   #dfs(2)동작
   def dfs(2):
     visited[2] = 1   #visited = [0, 1, 1, 0, 0, 0, 0]이 됨
     for i in amap[2]:   #amap[2]인 1, 5를 하나씩 검사
       if not visited[5]:   # visited[1] = 1이므로 False
         dfs(5)   #dfs(5)호출

   #dfs(5)동작
   def dfs(5):
     visited[5] = 1   #visited = [0, 1, 1, 0, 0, 1, 0]이 됨
     ...
     ...
     
   결국 첫 for loof의 i가 1인 상황이 종료되면 cnt += 1이 실행되어
   [1,2,5]노드가 하나의 연결노드임이 확인되고, 위 과정을 반복하여
   [3,4,6]노드가 하나의 연결노드임이 확인되면서 cnt +=1 가 실행된다.
   👉🏻 결과는 cnt = 2 연결노드는 2개이다
```

* * *

### 📚정리


❓DFS 동작원리

보통 DFS는 한 노드를 중점으로 ```dfs(start, end, depth)```형태로,
for loof에서 i를 증가시키면서 ```dfs(i, end, depth)```를 호출하면서
```start == end``` 일 때 depth를 저장 or return 하는 경우가 대부분이다.

```python
#이런느낌
dfs(start, end, depth):

  if start == end:
    return depth
    
  for i in map[start]:
    dfs(i, end, depth)  #start를 i로 잡아서 재귀함수로  반복호출
```
그러나 이번 예제와 같이, ```for loof```으로 ```dfs()```호출 횟수를 조절하는 일종의 **Back-Tracking** 알고리즘을 함께 사용하여, **DFS**호출을 줄이는 방법이 일반적으로 많이 사용된다.

#### ✍🏻 결론, 
   - 어느부분에서 **DFS**로 가지치기를 진행할지, 
   - 그리고 어떤부분을 **Back-Tracking**으로 제약을걸지 가 관건이다!