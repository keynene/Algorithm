# [Silver II] 촌수계산 - 2644 

[문제 링크](https://www.acmicpc.net/problem/2644) 

### 성능 요약

메모리: 113112 KB, 시간: 108 ms

### 분류

그래프 이론(graphs), 그래프 탐색(graph_traversal), 너비 우선 탐색(bfs), 깊이 우선 탐색(dfs)

### 문제 설명

<p>우리 나라는 가족 혹은 친척들 사이의 관계를 촌수라는 단위로 표현하는 독특한 문화를 가지고 있다. 이러한 촌수는 다음과 같은 방식으로 계산된다. 기본적으로 부모와 자식 사이를 1촌으로 정의하고 이로부터 사람들 간의 촌수를 계산한다. 예를 들면 나와 아버지, 아버지와 할아버지는 각각 1촌으로 나와 할아버지는 2촌이 되고, 아버지 형제들과 할아버지는 1촌, 나와 아버지 형제들과는 3촌이 된다.</p>

<p>여러 사람들에 대한 부모 자식들 간의 관계가 주어졌을 때, 주어진 두 사람의 촌수를 계산하는 프로그램을 작성하시오.</p>

### 입력 

 <p>사람들은 1, 2, 3, …, n (1 ≤ n ≤ 100)의 연속된 번호로 각각 표시된다. 입력 파일의 첫째 줄에는 전체 사람의 수 n이 주어지고, 둘째 줄에는 촌수를 계산해야 하는 서로 다른 두 사람의 번호가 주어진다. 그리고 셋째 줄에는 부모 자식들 간의 관계의 개수 m이 주어진다. 넷째 줄부터는 부모 자식간의 관계를 나타내는 두 번호 x,y가 각 줄에 나온다. 이때 앞에 나오는 번호 x는 뒤에 나오는 정수 y의 부모 번호를 나타낸다.</p>

<p>각 사람의 부모는 최대 한 명만 주어진다.</p>

### 출력 

 <p>입력에서 요구한 두 사람의 촌수를 나타내는 정수를 출력한다. 어떤 경우에는 두 사람의 친척 관계가 전혀 없어 촌수를 계산할 수 없을 때가 있다. 이때에는 -1을 출력해야 한다.</p>

### 📖[Python/파이썬][🥈2] 백준 알고리즘 2644 - 촌수계산
### 📜문제
![](https://velog.velcdn.com/images/keynene/post/a5d47cce-1e85-420c-b2b1-b99b591d0674/image.png)
![](https://velog.velcdn.com/images/keynene/post/c877a957-0eaa-47ee-ad3f-6af2efb10511/image.png)
![](https://velog.velcdn.com/images/keynene/post/f25525c8-44e7-43d8-a1a5-5ef2fe6ab4eb/image.png)

* * *

#### DFS(깊이우선탐색)
그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘
<span style="color:green">#Stack #스택 #재귀 #순환 #무한루프탈출 #Back-Tracking</span>

#### BFS(넓이우선탐색)
그래프에서 가까운 노드부터 우선적으로 탐색하는 알고리즘
<span style="color:green">#Queue #큐</span>

* * *

### 📕풀이방향
#### DFS알고리즘
n,s(start),e(end),m,노드들을 저장하고, ```dfs()```함수를 통해 ```start==end```일 때, dep을 출력하자


#### BFS알고리즘
n,s(start),e(end),m,노드들을 저장하고, ```bfs()```함수를 통해 res에 촌수를 저장해가면서
큐가 비었을 때 res를 출력하자




* * *

### 📝알고리즘 구현순서
#### DFS알고리즘
1. n,s(start),e(end),m,노드들을 **MAP**으로 인덱싱하여 저장, visited(list)를 ```1e9```로 초기화하여
```dfs()```에서 ```start == end```일 때, visited[end]값을 출력하자
```
❓ visited를 1e9로 초기화하는 이유

  dfs()를 호출할 때마다 dep를 증가시켜서 파라미터로 넘길껀데,
  visited[end]에 저장된 값과 dep를 비교하여 
  더 작은 값을 최종 visited[end]에 넣어 반환할꺼니까!
```
#### BFS알고리즘

1. n,s(start),e(end),m,노드들을 **MAP**으로 인덱싱하여 저장, visited(list)를 ```False```로, res(list)를 초기화하자
2. ```bfs()```에 ```start```값을 큐에 넣어, 하나씩 꺼내면서 방문한적이 없으면 res를 증가시키자
3. ```bfs()```함수 종료 후 ```res[end] > 0```이면 방문한적이 있다는 뜻이므로 호출,
   아니면 "-1"을 출력하자

* * *

### 💻결과코드
#### DFS알고리즘
```python
import sys
input = sys.stdin.readline

n = int(input().rstrip())
start,end = map(int, input().split())
m = int(input().rstrip())
node = [map(int, input().split())for _ in range(m)]
visited = [1e9]*(n+1)

#인덱싱하기
amap = [[] for _ in range(n+1)]
for x,y in node:
    amap[x].append(y)
    amap[y].append(x)

#DFS
def dfs(start, end, amap, dep):
    if start == end:
        visited[end] = min(visited[end],dep)
        return

    for i in amap[start]:
    	#방문한 적이 없으면 방문하여 dep 저장
        if visited[i] > dep:
            visited[i] = dep
            dfs(i, end, amap, dep+1)

dfs(start, end, amap, 1)

#visited[end]값이 1e9이면 방문한 적이 없다는 뜻이니까
if visited[end] == 1e9:
    print(-1)
else:
    print(visited[end])
```
* * *
#### BFS알고리즘
```python
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
start, end = map(int, input().split())
m = int(input())
node = [list(map(int, input().split())) for _ in range(m)]
visited = [False]*(n+1)
res = [0]*(n+1)

#인덱싱하기
rel = [[] for _ in range(n+1)]
for u,v in node:
    rel[u].append(v)
    rel[v].append(u)

#BFS
def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = True
	
    #큐가 빌 때까지 실행
    while queue:
    	#제일 먼저 들어온 값부터 검사
        v = queue.popleft()
        
        for i in rel[v]:
            if not visited[i]:
                queue.append(i)
                #함수 밖에 있는 res에 현재노드(v)와의 촌수를 저장
                res[i] = res[v]+1
                visited[i] = True

bfs(start)
#res[end]값이 0이면 방문한 적이 없다는 뜻이니까
if res[end] > 0:
    print(res[end])
else:
    print(-1)
```

* * *

### 📚정리
[내 포스팅 : [Python/파이썬][🥈2] 백준 알고리즘 1260 - DFS와 BFS](https://velog.io/@keynene/Python%ED%8C%8C%EC%9D%B4%EC%8D%AC2-%EB%B0%B1%EC%A4%80-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-1260-DFS%EC%99%80-BFS)
1. **DFS와 BFS**중 선택, **인덱싱/인접행렬**중 선택이 관건인 것 같다.
   (위 포스팅에서 다뤘듯이 방법이 너무 다양해서 설계 시 방법을 **선택**하는 것이 관건)