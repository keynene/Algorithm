# [Silver II] DFS와 BFS - 1260 

[문제 링크](https://www.acmicpc.net/problem/1260) 

### 성능 요약

메모리: 125724 KB, 시간: 200 ms

### 분류

그래프 이론(graphs), 그래프 탐색(graph_traversal), 너비 우선 탐색(bfs), 깊이 우선 탐색(dfs)

### 문제 설명

<p>그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.</p>

### 입력 

 <p>첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.</p>

### 출력 

 <p>첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.</p>

## 📖[Python/파이썬][🥈2] 백준 알고리즘 1260 - DFS와 BFS
### 📜문제
![](https://velog.velcdn.com/images/keynene/post/4ea5dc5d-6b76-4737-b8ea-91639fcf742c/image.png)
![](https://velog.velcdn.com/images/keynene/post/c3b49c6c-a9fc-4180-a7f3-fac4269d826b/image.png)

* * *

#### DFS(깊이우선탐색)
그래프에서 **깊은 부분**을 우선적으로 탐색하는 알고리즘
<span style="color:green">#Stack #스택 #재귀 #순환 #무한루프탈출 #Back-Tracking</span>

#### BFS(넓이우선탐색)
그래프에서 **가까운 노드**부터 우선적으로 탐색하는 알고리즘
<span style="color:green">#Queue #큐 </span>

* * *


**DFS알고리즘**은 수차례 연습으로 이제 익숙해졌고, **BFS알고리즘**을 이번 문제로 처음 접하게 되었다.
우선, 다른사람의 풀이를 여러 차례 살펴보니 2가지 풀이방법이 있다는 것을 알게되었다.

#### 1. MAP형식으로 인덱스 기준으로 각 노드의 연결을 직관적으로 나타내기 
👉🏻 **수열+DFS/BFS** 등 직관적으로 연결노드의 번호를 이용할 때
👉🏻 **CYCLE 여부** 를 확인할 때
```python
 ex) 1-2-3 cycle로 연결되어있으면
    amap = [[2,3], [1,3], [1,2]]
    amap[1] = [2,3]  #1번 노드와 연결되어 있는 노드들 (idx == 1)
    amap[2] = [1,3]  #2번 노드와 연결되어 있는 노드들 (idx == 2)
    amap[3] = [1,2]  #3번 노드와 연결되어 있는 노드들 (idx == 3)
```
#### 2. MATRIX처럼 각 노드에 연결되어 있는 간선을 인접행렬 형태로 나타내기
👉🏻 **미로찾기, 영역구하기** 등 매트릭스 형식을 이용할 때
```python
 ex) 1-2-3 cycle로 연결되어있으면
    matrix = [[0,0,0,0], [0,0,1,1], [0,1,0,1], [0,1,1,0]]
    matrix[1] = [0,0,1,1]  #1번 노드와 연결되어 있는 노드들의 간선 (idx == 1)
    matrix[2] = [0,1,0,1]  #2번 노드와 연결되어 있는 노드들의 간선 (idx == 2)
    matrix[2] = [0,1,1,0]  #2번 노드와 연결되어 있는 노드들의 간선 (idx == 2)
```

* * *
### 📕풀이방향
앞서 설명한 2가지 풀이방법으로 다 풀어보았다.
1. **MAP**을 이용한 풀이
2. **MATRIX**를 이용한 풀이
   
* * *

### 📝알고리즘 구현순서
#### 1번풀이(MAP)
 1. n,m,v 입력받고 주어지는 노드 node(list)를, **map형식**으로 저장 후 정렬하자
 2. DFS, BFS 함수 정의 후 호출
 
#### 2번풀이(MATRIX)
 1. n,m,v 입력받고 주어지는 노드 node(list)를, **matrix형식**으로 0, 1로 구분하여 저장하자
 2. DFS, BFS 함수 정의 후 호출
 
 * * *
 
###  💻결과코드
#### ✏️1번풀이(MAP)
```python
import sys
from collections import deque
input = sys.stdin.readline

n,m,v = map(int, input().split())
node = [list(map(int, input().split())) for _ in range(m)]
amap = [[] for _ in range(n+1)]

#amap에 매핑
for x,y in node:
    amap[x].append(y)
    amap[y].append(x)

#amap 정렬
for i in range(1,n+1):
    amap[i].sort()

#DFS
d_visited = [False]*(n+1)
def dfs(v):
    print(v, end=' ')
    d_visited[v] = True   #호출된 v 방문처리
    for i in amap[v]:   #amap[v]에 저장된 노드들 하나씩
        if not d_visited[i]:   #방문검사하면서
            dfs(i)             #DFS 호출

#BFS
b_visited = [False]*(n+1)
def bfs(v):
    queue = deque([v])   #큐에 v 넣기
    b_visited[v] = True   #v 방문처리

    while queue:   #큐가 빌 때까지 반복
        v = queue.popleft()   #가장 먼저 들어온 노드 꺼내기 pop
        print(v, end=' ')   #선입선출이므로, pop된 노드 출력

        for i in amap[v]:   #amap[v]에 저장된 노드들 하나씩
            if not b_visited[i]:   #방문검사하면서
                queue.append(i)   #큐에 삽입하고
                b_visited[i] = True   #방문처리하기
        #이 때 큐가 비지 않았으면 다시 while queue에서 반복!!

dfs(v)
print()
bfs(v)
```

#### ✏️2번풀이(MATRIX)
```python
import sys
from collections import deque
input = sys.stdin.readline

n,m,v = map(int, input().split())
node = [list(map(int, input().split())) for _ in range(m)]
matrix = [[0]*(n+1) for _ in range(n+1)] #인접행렬

#노드들 간 간선을 1로 매핑
for x,y in node:
    matrix[y][x] = matrix[x][y] = 1

#DFS
d_visited = [False]*(n+1)
def dfs(v):
    print(v, end=' ')
    d_visited[v] = True

    for i in range(1, n+1):
    	#i노드에 방문하지 않았고, 현재노드(v)와 i노드 간의 선이 있을 경우 dfs호출
        if not d_visited[i] and matrix[v][i]:
            dfs(i)
            
            
##########################################################################
❓visited를 2차원이 아니라 1차원배열로 지정하는 이유

  Map은 '노드'가 중점인 반면, Matrix는 0과 1이 모두 '간선'이 주체이기 때문!
  
  visited를 2차원배열로 정의해도 조건문을 잘 작성하여 검사하면 되겠지만,
  1차원배열로 정의하면, 
  "if not visited[1]: " 는 '노드'가 주체가 되어, 
  1번 '노드'에 방문한 적이 있는지 검사하게 되기 때문에 간편함
##########################################################################



#BFS
b_visited = [False]*(n+1)
def bfs(v):
    queue = deque([v])
    b_visited[v] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')

        for i in range(1, n+1):
            if not b_visited[i] and matrix[v][i] == 1:
                queue.append(i)
                b_visited[i] = True

dfs(v)
print()
bfs(v)
```

* * *

### 📚정리
동작 원리는 위 코드에서 설명했으니 생략한다.

1. **DFS/BFS알고리즘** 모두 다양한 풀이법이 있다. (Map, Matrix 이외에도 많을 것)
2. **깊이**기준으로 탐색해야하면 **DFS**, **넓이(가까운)**기준으로 탐색하면 **BFS**로 풀이할 것