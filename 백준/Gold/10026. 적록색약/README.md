# [Gold V] 적록색약 - 10026 

[문제 링크](https://www.acmicpc.net/problem/10026) 

### 성능 요약

메모리: 267652 KB, 시간: 256 ms

### 분류

너비 우선 탐색(bfs), 깊이 우선 탐색(dfs), 그래프 이론(graphs), 그래프 탐색(graph_traversal)

### 문제 설명

<p>적록색약은 빨간색과 초록색의 차이를 거의 느끼지 못한다. 따라서, 적록색약인 사람이 보는 그림은 아닌 사람이 보는 그림과는 좀 다를 수 있다.</p>

<p>크기가 N×N인 그리드의 각 칸에 R(빨강), G(초록), B(파랑) 중 하나를 색칠한 그림이 있다. 그림은 몇 개의 구역으로 나뉘어져 있는데, 구역은 같은 색으로 이루어져 있다. 또, 같은 색상이 상하좌우로 인접해 있는 경우에 두 글자는 같은 구역에 속한다. (색상의 차이를 거의 느끼지 못하는 경우도 같은 색상이라 한다)</p>

<p>예를 들어, 그림이 아래와 같은 경우에</p>

<pre>RRRBB
GGBBB
BBBRR
BBRRR
RRRRR</pre>

<p>적록색약이 아닌 사람이 봤을 때 구역의 수는 총 4개이다. (빨강 2, 파랑 1, 초록 1) 하지만, 적록색약인 사람은 구역을 3개 볼 수 있다. (빨강-초록 2, 파랑 1)</p>

<p>그림이 입력으로 주어졌을 때, 적록색약인 사람이 봤을 때와 아닌 사람이 봤을 때 구역의 수를 구하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 N이 주어진다. (1 ≤ N ≤ 100)</p>

<p>둘째 줄부터 N개 줄에는 그림이 주어진다.</p>

### 출력 

 <p>적록색약이 아닌 사람이 봤을 때의 구역의 개수와 적록색약인 사람이 봤을 때의 구역의 수를 공백으로 구분해 출력한다.</p>

## 📖[Python/파이썬][🥇5] 백준 알고리즘 10026 - 적록색약
### 📜문제
![](https://velog.velcdn.com/images/keynene/post/c1046541-6b36-4861-a693-ca041162dfbf/image.png)
![](https://velog.velcdn.com/images/keynene/post/1511f9cd-a0c6-4532-9e6a-fe97b41ac83b/image.png)

* * *

#### DFS(깊이우선탐색)
임의의 한 노드에서 시작해서 다음 분기로 넘어가기 전에 해당 분기를 완벽하게 탐색하는 방법
<span style="color:green">#재귀 #순환 #무한루프탈출 #Back-Tracking</span>

* * *

### 📕풀이방향
[내 포스팅 : [Python/파이썬] [🥈1] 백준 알고리즘 2583 - 영역 구하기](https://velog.io/@keynene/Python%ED%8C%8C%EC%9D%B4%EC%8D%AC-1-%EB%B0%B1%EC%A4%80-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-2583-%EC%98%81%EC%97%AD-%EA%B5%AC%ED%95%98%EA%B8%B0)
이전 포스팅과 같이 **4방향 탐색 DFS**로도 접근가능하지만, 
**dx, dy를 이용한 DFS알고리즘** 으로 풀이해보려 한다.

n, RGB정보를 입력받아 저장하고 visited(방문확인용 list)를 <span style="color:red">False</span>로 초기화하여,
visited가 False일 때 ```dfs(x,y)```실행 후 <span style="color:blue">True</span>로 저장하면서 각 영역의 개수를 카운팅하자

❕❗주의사항
적록색약이 아닌 사람은 'R', 'G'를 서로 다른 영역으로 인지하고,
적록색약인 사람은 'R', 'G'를 하나의 영역으로 인지한다.

이를 주의하여 구현하자

* * *

### 📝알고리즘 구현순서
1. n과 rgb정보를 amap(list) 저장하여 ```for loof```을 이용해 
우선 **적록색약이 아닌사람의 영역을 카운팅**하자
2. ```for loof```을 이용해 amap에 <span style="color:red">'R'을 'G'로 바꿔주고</span>
**적록색약인 사람의 영역을 카운팅**하자

* * *

### 💻결과코드
```python
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

#영역구하기
def dfs(x,y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited[y][x] = True
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<n and 0<=ny<n and amap[y][x] == amap[ny][nx] and not visited[ny][nx]:
            dfs(nx,ny)

#입력값 받아 저장하기
n = int(input().rstrip())
amap = [list(map(str, input().rstrip())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]
acnt = 0   #적록색약 아닌사람용 카운팅 변수
rgcnt = 0  #적록색약인 사람용 카운팅 변수

#적록색약이 아닌 사람 dfs()호출하면서 영역 개수 카운팅
for y in range(n):
    for x in range(n):
        if not visited[y][x]:
            dfs(x,y)
            acnt += 1

#'R' → 'G' : 적록색약인 사람용 map만들기 (적록색약 : R==G 이므로)
for y in range(n):
    for x in range(n):
        if amap[y][x] == 'R':
            amap[y][x] = 'G'

#적록색약인 사람 dfs()호출하면서 영역 개수 카운팅
visited = [[False]*n for _ in range(n)]
for y in range(n):
    for x in range(n):
        if not visited[y][x]:
            dfs(x,y)
            rgcnt += 1

print(acnt, rgcnt)
```

* * *

#### ✏️1. n, rgb정보 저장 후 적록색약 아닌 사람의 영역개수 카운팅
```python
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)  #dfs깊이 늘리기 (백준은 1000이라 런타임에러나니까)

#영역 개수 구하기
def dfs(x,y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited[y][x] = True  #재방문하지 않도록 방문흔적 남기기
    
    #아래 dx,dy만의 for loof을 이용하여 dfs가 4번 재호출 되는걸 방지
    #필자는 이전까지 dfs(x-1,y), dfs(x+1,y) 이런식으로 4번 호출했었음...
    for i in range(4):
        nx = x+dx[i]  #x+dx[i] 로 현재의 nx값 저장
        ny = y+dy[i]  #y+dy[i] 로 현재의 ny값 저장
        
        #현재 nx,ny가 map영역을 벗어나지 않거나, 방문흔적이 없을때만 dfs호출
        if 0<=nx<n and 0<=ny<n and amap[y][x] == amap[ny][nx] and not visited[ny][nx]:
            dfs(nx,ny)

n = int(input().rstrip())
amap = [list(map(str, input().rstrip())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]
acnt = 0

#적록색약이 아닌 사람 영역 개수 카운팅
for y in range(n):
    for x in range(n):
        if not visited[y][x]: #방문흔적이 없으면
            dfs(x,y)          #dfs(x,y)호출하여 방문흔적 남기고,
            acnt += 1         #영역 개수 카운팅
```

* * *

#### ✏️2. 적록색약용 map만들고, 적록색약인 사람의 영역개수 카운팅
```python
#dfs내용은 위 1번과 같음
def dfs(x,y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited[y][x] = True
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<n and 0<=ny<n and amap[y][x] == amap[ny][nx] and not visited[ny][nx]:
            dfs(nx,ny)

#적록색약용 map만들기 (amap의 R→G)
#적록색약은 R==G로 인식하기 때문!
for y in range(n):
    for x in range(n):
        if amap[y][x] == 'R':
            amap[y][x] = 'G'

#적록색약의 영역 개수 카운팅
rgcnt = 0
visited = [[False]*n for _ in range(n)]  #위에서 더럽힌 방문흔적 초기화
for y in range(n):
    for x in range(n):
        if not visited[y][x]:
            dfs(x,y)
            rgcnt += 1

print(acnt, rgcnt)

```

* * *

### 📚초기 알고리즘과 정리
#### 🙋🏻‍♀️1번째 초기 코드 아이디어

```
1. 일단 R,G,B로 하면 뭔가 오류가 있을 것 같으니까 R=0, B=1, G=2로 보기좋게 매핑하자
(왜??? 아직 저렇게 생각한 이유를 모르겠음.. 그래도 문자든 숫자든 취향차이니까 넘어가자..)

2. 그리고 for loof 한 번에 적록색약인 사람과 적록색약이 아닌 사람의 map을 
"한꺼번에"확인하면서 카운팅하고싶다.
(같은 깊이의 for loof은 1번이든 2번이든 시간복잡도는 똑같은데... 그래도 접근은 좋다)

3. 적록색약인 사람과 적록색약이 아닌사람의 map을 따로 만들자 - 한꺼번에 돌려야 하니까
(list 메모리 2배로 잡아먹고~🤦🏻‍♀️)

4. dfs에서 방문한 영역은 amap/rgmap에 3으로 매핑하자 - 재방문하면 안되니까
(visited 리스트를 만들어서 체크하면 원래의 amap/rgmap이 더러워지지 않을텐데)
```
#### 코드
```python
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

n = int(input().rstrip())
graph = [list(input().rstrip()) for _ in range(n)]
amap = []
rgmap = []
acnt = 0
rgcnt = 0

#영역 개수 구하기
#4번째 파라미터로 현재의 숫자(num)를 받음으로써, num이 아닌 곳은 검사하지 않음
def dfs(x,y,map,num):
    if x<0 or y<0 or x>=n or y>=n:
        return
    if map[y][x] == 3 and map[y][x] != num:
        return
    elif map[y][x] == num:
        map[y][x] = 3
        dfs(x-1,y,map,num)
        dfs(x,y-1,map,num)
        dfs(x+1,y,map,num)
        dfs(x,y+1,map,num)
        return
    else:
        return

#적록색약 아닌사람용, 적록색약용 map 만들기
for rgb in graph:
    string = 0
    num = ''    #적록색약이 아닌사람의 amap에 매핑될 str
    rgnum = ''  #적록색약인 사람의 rgmap에 매핑될 str
    for string in rgb:
        if string == 'R':
            num += str(0)+' '
            rgnum += str(0)+' '  #적록색약은 R==G니까
        elif string == 'B':
            num += str(1)+' '
            rgnum += str(1)+' '
        elif string == 'G':
            num += str(2)+' '
            rgnum += str(0)+' '  #적록색약은 R==G니까
    amap.append(list(map(int, num.split())))
    rgmap.append(list(map(int, rgnum.split())))

#amap, rgmap 동시에 돌리면서 영역구하고 방문한 영역은 3으로 매핑
for y in range(n):
    for x in range(n):
        if amap[y][x] != 3:
            dfs(x,y,amap,amap[y][x])  
            acnt += 1
        if rgmap[y][x] != 3:
            dfs(x,y,rgmap,rgmap[y][x])
            rgcnt += 1

print(acnt, rgcnt, sep=' ')
```

* * *

#### 🙋🏻‍♀️2번째 초기 코드 아이디어
R=0, B=1, G=2 매핑하는 건 똑같고 동작도 똑같은데 visited를 추가했고,
```dfs()```안에서 R(0)→G(2)로 변경하여 적록색약용 map으로 만들었음
👉🏻결론 : 메모리는 더 잡아먹고 시간이 30ms 줄어듦🤣
```
1. for loof로 동시에 카운팅하는 아이디어는 버리고, visited를 만들자.
   적록색약이 아닌 사람의 amap을 dfs()로 검사하면서 방문흔적을 남기고,
   dfs()안에서 R을 찾아 G로 amap을 변경하여 적록색약용 map을 만들어주자
   (for loor를 두 번 돌긴 하지만 시간복잡도는 똑같아서 접근은 좋았으나..
   이러면서 dfs안에서 R일때의 조건식이 추가되어서... 취향차이 인걸로)
   
2. 만들어진 map을 이용하여 적록색약인 사람의 영역을 카운팅하자
```
#### 코드
```python
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n = int(input().rstrip())
rgb = [list(map(str, input().rstrip())) for _ in range(n)]
amap = []
visited = [[0 for _ in range(n)] for _ in range(n)]
cnt = 0
res = []

def dfs(x,y,num):
    if x<0 or y<0 or x>=n or y>=n:
        return
    if visited[y][x] == 1 or amap[y][x] != num:
        return
    elif amap[y][x] == num:
        visited[y][x] = 1
        if num == 2:
            amap[y][x] = 0
        dfs(x-1,y,num)
        dfs(x,y-1,num)
        dfs(x+1,y,num)
        dfs(x,y+1,num)
        return
    
for string in rgb:
    num = ''
    for al in string:
        if al == 'R':
            num += str(0)+' '
        elif al == 'B':
            num += str(1)+' '
        elif al == 'G':
            num += str(2)+' '
    amap.append(list(map(int, num.split())))

for y in range(n):
    for x in range(n):
        if not visited[y][x]:
            dfs(x,y,amap[y][x])
            cnt += 1
res.append(cnt)

cnt = 0
visited = [[0 for _ in range(n)] for _ in range(n)]
for y in range(n):
    for x in range(n):
        if not visited[y][x]:
            dfs(x,y,amap[y][x])
            cnt += 1
res.append(cnt)
print(*res)
```

* * *

#### 정리
1. 이런 과정을 거쳐 찾은 알고리즘이 제일 상단에 언급한 **dx,dy를 이용한 DFS 알고리즘**이고,
'문자 → 숫자' 치환하는 과정이 줄어들어 시간도 빨라졌다.
2. 그리고 원래 코드에서 문자를 저장했던 'rgb'라는 list가 최종 알고리즘에서는 그냥
map 그 자체가 되어버려서 rgb를 저장했던 메모리 낭비도 줄었다

정석으로 4방향 탐색하는 DFS알고리즘도 좋지만, dx,dy를 이용한 DFS알고리즘도 연습해보자
+첫 골드 문제를 못 푼게 좀 아쉽다.. 실버 문제랑 차원이 좀 다른 것 같다😅
