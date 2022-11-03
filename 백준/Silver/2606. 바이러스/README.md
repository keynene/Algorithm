# [Silver III] 바이러스 - 2606 

[문제 링크](https://www.acmicpc.net/problem/2606) 

### 성능 요약

메모리: 113112 KB, 시간: 108 ms

### 분류

그래프 이론(graphs), 그래프 탐색(graph_traversal), 너비 우선 탐색(bfs), 깊이 우선 탐색(dfs)

### 문제 설명

<p>신종 바이러스인 웜 바이러스는 네트워크를 통해 전파된다. 한 컴퓨터가 웜 바이러스에 걸리면 그 컴퓨터와 네트워크 상에서 연결되어 있는 모든 컴퓨터는 웜 바이러스에 걸리게 된다.</p>

<p>예를 들어 7대의 컴퓨터가 <그림 1>과 같이 네트워크 상에서 연결되어 있다고 하자. 1번 컴퓨터가 웜 바이러스에 걸리면 웜 바이러스는 2번과 5번 컴퓨터를 거쳐 3번과 6번 컴퓨터까지 전파되어 2, 3, 5, 6 네 대의 컴퓨터는 웜 바이러스에 걸리게 된다. 하지만 4번과 7번 컴퓨터는 1번 컴퓨터와 네트워크상에서 연결되어 있지 않기 때문에 영향을 받지 않는다.</p>

<p><img alt="" src="" style="width: 239px; height: 157px; "></p>

<p>어느 날 1번 컴퓨터가 웜 바이러스에 걸렸다. 컴퓨터의 수와 네트워크 상에서 서로 연결되어 있는 정보가 주어질 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에는 컴퓨터의 수가 주어진다. 컴퓨터의 수는 100 이하이고 각 컴퓨터에는 1번 부터 차례대로 번호가 매겨진다. 둘째 줄에는 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수가 주어진다. 이어서 그 수만큼 한 줄에 한 쌍씩 네트워크 상에서 직접 연결되어 있는 컴퓨터의 번호 쌍이 주어진다.</p>

### 출력 

 <p>1번 컴퓨터가 웜 바이러스에 걸렸을 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 첫째 줄에 출력한다.</p>

## 📖[Python/파이썬][🥈3] 백준 알고리즘 2606 - 바이러스
### 📜문제
![](https://velog.velcdn.com/images/keynene/post/120ebb06-5719-4180-9a0e-8de9391f4813/image.png)
![](https://velog.velcdn.com/images/keynene/post/c40aeabc-2307-4ea5-8c58-ed57dc25f542/image.png)

* * *

#### DFS(깊이우선탐색)
![](https://velog.velcdn.com/images/keynene/post/bccb3a9b-be02-48d3-8ae1-90bedfa53f2d/image.png)
- 임의의 한 노드에서 시작해서 다음 분기로 넘어가기 전에 해당 분기를 완벽하게 탐색하는 방법
- 자기 자신을 호출하는 재귀/순환 알고리즘의 형태임
- 노드 방문 여부를 검사해놔야 무한루프에 빠질 위험이 줄어듦
- 주로 백트래킹과 함께 쓰여, 모든 노드를 다 방문하는 것을 차단함

* * *

### 📕풀이방향

[내 포스팅 : [Python/파이썬] [🥈2] 백준 알고리즘 11724 - 연결 요소의 개수](https://velog.io/@keynene/Python%ED%8C%8C%EC%9D%B4%EC%8D%AC-2-%EB%B0%B1%EC%A4%80-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-11724-%EC%97%B0%EA%B2%B0-%EC%9A%94%EC%86%8C%EC%9D%98-%EA%B0%9C%EC%88%98)

이전에 포스팅한 "연결 요소의 개수"문제의 **DFS**개념과 풀이방법이 매우 흡사하다!
똑같이 입력값 저장, 노드를 **MAP** 형태로 저장하고, visited라는 빈 list를 만들어,
```dfs(i)``` 함수로 방문검사를 하면서 첫 방문시 ```visited[i]=1``` 체크해주면 된다.
다만, 이전포스팅과 달라진 점은 <span style="color:red">1번 컴퓨터가 웜바이러스에 걸렸을 때만</span> 검사하면 된다.
그리고 ```sum(visited)-1```을 출력해주면 끝! (1컴퓨터 자신은 빼야하니까)

```👉🏻 ex) n=7일 때 1-2-3-4만 연결되어 있으면, 5-6-7은 웜바이러스 걸렸든 말든 검사할 필요가 없음!```

* * *

### 📝알고리즘 구현순서
1. n,m과 node를 입력받으면서 amap에 map형태로 저장하자
2. visited list를 0으로 초기화하고 ```dfs()```함수를 만들고, ```for loof```로 <span style="color:red">amap[1]의 요소(i)만 </span>
   ```dfs(i)```를 호출하자
   👉🏻 1번에 연결되어있는 컴퓨터들만 확인하면, 나머지 컴퓨터는 웜바이러스 걸리든말든 상관X
      (```for loof```로 i를 1~n까지 다 돌 필요가 없음)

* * *

### 💻결과코드
```python
import sys
input = sys.stdin.readline

n = int(input().rstrip())
m = int(input().rstrip())
node = [list(map(int, input().split())) for _ in range(m)]
amap = [[] for _ in range(n+1)]
visited = [0]*(n+1)

for u,v in node:
    amap[u].append(v)
    amap[v].append(u)

def dfs(v):
    visited[v] = 1
    for i in amap[v]:
        if not visited[i]:
            dfs(i)

for i in amap[1]:
    if not visited[i]:
        dfs(i)

print(sum(visited)-1)   #1번컴퓨터 자신 카운팅은 빼주기
```

* * *

#### ✏️1. n, m, node 입력받으면서 amap 저장
```python
import sys
input = sys.stdin.readline

n = int(input().rstrip())
m = int(input().rstrip())
node = [list(map(int, input().split())) for _ in range(m)]
amap = [[] for _ in range(n+1)]

#Graph 형식으로 저장
for u,v in node:
    amap[u].append(v)
    amap[v].append(u)
```

* * *

#### ✏️2. dfs()함수 구현과 for loof에서 호출
```python
visited = [0]*(n+1)


def dfs(v):
    visited[v] = 1      #방문안한 노드마다 방문기록 0 → 1 
    for i in amap[v]:   #해당 노드와 연결된 노드들 방문검사
        if not visited[i]:
            dfs(i)

for i in amap[1]:       #amap[1] 요소만 검사하면 됨
    if not visited[i]:
        dfs(i)

print(sum(visited)-1)   #1번컴퓨터 카운팅 빼기
```
```
❓"for i in amap[1]"만 검사하는 이유

알고리즘 구현순서 1번에서 amap으로 [1]번 컴퓨터와 연결된 노드를 amap[1]에 저장해뒀기 때문!

amap[1] = 2, 5
amap[2] = 1, 3, 5
...
...
amap[7] = 4

이렇게 인덱싱 해뒀기 때문에 amap[1]은 1번컴퓨터의 연결노드만 검사함
```

* * *

### 📚정리
[내 포스팅 : [Python/파이썬] [🥈2] 백준 알고리즘 11724 - 연결 요소의 개수](https://velog.io/@keynene/Python%ED%8C%8C%EC%9D%B4%EC%8D%AC-2-%EB%B0%B1%EC%A4%80-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-11724-%EC%97%B0%EA%B2%B0-%EC%9A%94%EC%86%8C%EC%9D%98-%EA%B0%9C%EC%88%98)

이전 포스팅에서 다뤄봤던 유형의 **DFS** 개념이라 풀이하기 수월했다.
이전 포스팅에서도 언급한대로, **DFS** 라고해서 ```dfs()```함수 안에서 무조건 해결하려고 하지말고,
- **DFS**를 어떤시점에서 호출할지, 
- 호출했을 때는 또 어떤부분에서 return, 즉 종료할지 

를 생각하면서 알고리즘을 설계하자!