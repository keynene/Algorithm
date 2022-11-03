# [Gold III] 텀 프로젝트 - 9466 

[문제 링크](https://www.acmicpc.net/problem/9466) 

### 성능 요약

메모리: 401340 KB, 시간: 1944 ms

### 분류

깊이 우선 탐색(dfs), 그래프 이론(graphs), 그래프 탐색(graph_traversal)

### 문제 설명

<p>이번 가을학기에 '문제 해결' 강의를 신청한 학생들은 텀 프로젝트를 수행해야 한다. 프로젝트 팀원 수에는 제한이 없다. 심지어 모든 학생들이 동일한 팀의 팀원인 경우와 같이 한 팀만 있을 수도 있다. 프로젝트 팀을 구성하기 위해, 모든 학생들은 프로젝트를 함께하고 싶은 학생을 선택해야 한다. (단, 단 한 명만 선택할 수 있다.) 혼자 하고 싶어하는 학생은 자기 자신을 선택하는 것도 가능하다.</p>

<p>학생들이(s<sub>1</sub>, s<sub>2</sub>, ..., s<sub>r</sub>)이라 할 때, r=1이고 s<sub>1</sub>이 s<sub>1</sub>을 선택하는 경우나, s<sub>1</sub>이 s<sub>2</sub>를 선택하고, s<sub>2</sub>가 s<sub>3</sub>를 선택하고,..., s<sub>r-1</sub>이 s<sub>r</sub>을 선택하고, s<sub>r</sub>이 s<sub>1</sub>을 선택하는 경우에만 한 팀이 될 수 있다.</p>

<p>예를 들어, 한 반에 7명의 학생이 있다고 하자. 학생들을 1번부터 7번으로 표현할 때, 선택의 결과는 다음과 같다.</p>

<table class="table table-bordered" style="width:30%">
	<thead>
		<tr>
			<th>1</th>
			<th>2</th>
			<th>3</th>
			<th>4</th>
			<th>5</th>
			<th>6</th>
			<th>7</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>3</td>
			<td>1</td>
			<td>3</td>
			<td>7</td>
			<td>3</td>
			<td>4</td>
			<td>6</td>
		</tr>
	</tbody>
</table>

<p>위의 결과를 통해 (3)과 (4, 7, 6)이 팀을 이룰 수 있다. 1, 2, 5는 어느 팀에도 속하지 않는다.</p>

<p>주어진 선택의 결과를 보고 어느 프로젝트 팀에도 속하지 않는 학생들의 수를 계산하는 프로그램을 작성하라.</p>

### 입력 

 <p>첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스의 첫 줄에는 학생의 수가 정수 n (2 ≤ n ≤ 100,000)으로 주어진다. 각 테스트 케이스의 둘째 줄에는 선택된 학생들의 번호가 주어진다. (모든 학생들은 1부터 n까지 번호가 부여된다.)</p>

### 출력 

 <p>각 테스트 케이스마다 한 줄에 출력하고, 각 줄에는 프로젝트 팀에 속하지 못한 학생들의 수를 나타내면 된다.</p>

## 📖[Python/파이썬][🥇3] 백준 알고리즘 9466 - 텀 프로젝트
### 📜문제
![](https://velog.velcdn.com/images/keynene/post/32f746c1-018c-4b19-b142-9686d307cae8/image.png)
![](https://velog.velcdn.com/images/keynene/post/57606927-3d5c-4a24-95c7-f8af46dde7cf/image.png)

* * *

#### DFS(깊이우선탐색)

임의의 한 노드에서 시작해서 다음 분기로 넘어가기 전에 해당 분기를 완벽하게 탐색하는 방법
<span style="color:green">#재귀 #순환 #무한루프탈출 #Back-Tracking</span>

* * *

### 📕풀이방향
[내 포스팅 : [Python/파이썬][🥈1] 백준 알고리즘 14888 - 연산자 끼워넣기](https://velog.io/@keynene/Python%ED%8C%8C%EC%9D%B4%EC%8D%AC1-%EB%B0%B1%EC%A4%80-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-14888-%EC%97%B0%EC%82%B0%EC%9E%90-%EB%81%BC%EC%9B%8C%EB%84%A3%EA%B8%B0)
이전 포스팅과 비슷한 **DFS알고리즘 + 수열** 문제이다.

우선 테스트케이스만큼 실행되므로 하나의 케이스의 동작은 T만큼 반복하는```for loof```안에서 구현하자
n, number(선택된학생 리스트)를 입력받고, visited(list)와 result(list)를 입력받자
i가 1~n까지 반복하는 ```for loof```에서 ```visited[i] == False```이면 ```dfs(v)```를 실행하자
```dfs(v)```는 방문처리를 함과 동시에 cycle을 이루는 학생들을 반환해주는 함수로 구현하자

* * *

### 📝알고리즘 구현순서
1. n, number(선택된학생 리스트), visited(list), result(list)초기화하고,
   방문 안 한 노드를 ```dfs(i)```로 호출하여 cycle이 되는 학생리스트를 result에 추가하자
   
* * *

### 💻결과코드
```python
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

#cycle 이루는 result 반환
def dfs(v):
    global result
    visited[v] = True
    cycle.append(v)
    num = number[v]

    if visited[num]:
        if num in cycle:
            result += cycle[cycle.index(num):]
        return
    else:
        dfs(num)

#테스트 케이스만큼 실행
for _ in range(int(input().rstrip())):
    N = int(input().rstrip())
    number = [0] + list(map(int, input().split()))
    visited = [True] + [False]*N
    result = []
	
    #1~n까지 방문여부 확인하면서 dfs()호출
    for i in range(1,N+1):
        if not visited[i]:
            cycle = []
            dfs(i)

    print(N-len(result))
```

* * *

#### ✏️1. 입력받고, dfs()함수, cycle리스트 구현
```python
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

#cycle 이루는 result 반환
def dfs(v):
    global result      #global이므로 result dfs()밖으로 반환 가능
    visited[v] = True  #방문체크
    cycle.append(v)    #cycle에 v추가
    num = number[v]    #num = v가 선택한 학생

    if visited[num]:   #선택된 학생노드를 방문한 적이 있으면
        if num in cycle:  #dfs()에서 만든 임시cycle에 num이 있는지 확인
            result += cycle[cycle.index(num):]  #result에 임시cycle추가
        return
    else:
        dfs(num)  #선택된 학생노드를 방문한 적잉 없으면 dfs(선택된학생)실행

#테스트 케이스만큼 실행
for _ in range(int(input().rstrip())):
    N = int(input().rstrip())
    number = [0] + list(map(int, input().split()))
    visited = [True] + [False]*N
    result = []

	#1~n까지 방문여부 확인하면서 dfs()호출
    for i in range(1,N+1):
        if not visited[i]:
            cycle = [] #cycle 초기화 (매 번호마다 팀이 되는 학생이 다르니까)
            dfs(i)

    print(N-len(result))  #팀이 안꾸려진 학생 수 출력
```
* * *

### 📚동작원리 및 정리
#### ❓동작원리
```python
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def dfs(v):
    global result
    visited[v] = True
    cycle.append(v)
    num = number[v]

    if visited[num]:
        if num in cycle:
            result += cycle[cycle.index(num):]
        return
    else:
        dfs(num)

for _ in range(int(input().rstrip())):
    N = int(input().rstrip())
    number = [0] + list(map(int, input().split()))
    visited = [True] + [False]*N
    result = []

    for i in range(1,N+1):
        if not visited[i]:
            cycle = []
            dfs(i)

    print(N-len(result))
```
전 코드를 차례대로 훑어보자
ex)
n = 7
number = 3 1 3 7 3 4 6

```
for loof부터 살펴보면,
 i = 1
 visited[1] = False이므로 dfs(i)호출
 👉🏻 dfs(1)
    visited[1] = True
    cycle.append(1)     #임시 cycle = [1]
    num = number[1]     #num = 3
    
    if visited[3]:    #방문안했으므로 X
    else dfs(3)
    
 👉🏻 dfs(3)
 	visited[3] = True
    cycle.append(3)     #임시 cycle = [1,3]
    num = number[3]     #num = 3
    
    if visited[3]:    #방문했으므로 O
      if 3 in cycle:    #cycle에 3 있으므로 O
        result = cycle[cycle.index(3):]  #현재 인덱스부터 끝까지 result에 저장
        return
        
```
❓```cycle[cycle.index(3):]```만 result에 저장하는 이유

cycle에  [1,3]이 있는데,
1의 number[1] = 3 / 3의 number[3] = 3 이므로
3만 팀을 꾸릴 수 있고, 1은 그 누가 원해도 절대로 팀을 꾸리지 못하기 때문이다.

* * *

#### 정리
1. ```list.index(x)``` : list에서의 x의 인덱스(순서)를 반환한다.




