# [Silver I] 영역 구하기 - 2583 

[문제 링크](https://www.acmicpc.net/problem/2583) 

### 성능 요약

메모리: 133852 KB, 시간: 148 ms

### 분류

너비 우선 탐색(bfs), 깊이 우선 탐색(dfs), 그래프 이론(graphs), 그래프 탐색(graph_traversal)

### 문제 설명

<p>눈금의 간격이 1인 M×N(M,N≤100)크기의 모눈종이가 있다. 이 모눈종이 위에 눈금에 맞추어 K개의 직사각형을 그릴 때, 이들 K개의 직사각형의 내부를 제외한 나머지 부분이 몇 개의 분리된 영역으로 나누어진다.</p>

<p>예를 들어 M=5, N=7 인 모눈종이 위에 <그림 1>과 같이 직사각형 3개를 그렸다면, 그 나머지 영역은 <그림 2>와 같이 3개의 분리된 영역으로 나누어지게 된다.</p>

<p style="text-align: center;"><img alt="" src="https://www.acmicpc.net/upload/images/zzJD2aQyF5Rm4IlOt.png" style="height:224px; width:589px"></p>

<p><그림 2>와 같이 분리된 세 영역의 넓이는 각각 1, 7, 13이 된다.</p>

<p>M, N과 K 그리고 K개의 직사각형의 좌표가 주어질 때, K개의 직사각형 내부를 제외한 나머지 부분이 몇 개의 분리된 영역으로 나누어지는지, 그리고 분리된 각 영역의 넓이가 얼마인지를 구하여 이를 출력하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 M과 N, 그리고 K가 빈칸을 사이에 두고 차례로 주어진다. M, N, K는 모두 100 이하의 자연수이다. 둘째 줄부터 K개의 줄에는 한 줄에 하나씩 직사각형의 왼쪽 아래 꼭짓점의 x, y좌표값과 오른쪽 위 꼭짓점의 x, y좌표값이 빈칸을 사이에 두고 차례로 주어진다. 모눈종이의 왼쪽 아래 꼭짓점의 좌표는 (0,0)이고, 오른쪽 위 꼭짓점의 좌표는(N,M)이다. 입력되는 K개의 직사각형들이 모눈종이 전체를 채우는 경우는 없다.</p>

### 출력 

 <p>첫째 줄에 분리되어 나누어지는 영역의 개수를 출력한다. 둘째 줄에는 각 영역의 넓이를 오름차순으로 정렬하여 빈칸을 사이에 두고 출력한다.</p>

## 📖[Python/파이썬][🥈1] 백준 알고리즘 2583 - 영역 구하기
### 📜문제
![](https://velog.velcdn.com/images/keynene/post/3002ea37-3ae6-4f68-90e0-4066046b3b97/image.png)
![](https://velog.velcdn.com/images/keynene/post/b7953ebb-419c-43f0-abab-23abf9566fd1/image.png)

* * *

#### DFS(깊이우선탐색)
![](https://velog.velcdn.com/images/keynene/post/bccb3a9b-be02-48d3-8ae1-90bedfa53f2d/image.png)
- 임의의 한 노드에서 시작해서 다음 분기로 넘어가기 전에 해당 분기를 완벽하게 탐색하는 방법
- 자기 자신을 호출하는 재귀/순환 알고리즘의 형태임
- 노드 방문 여부를 검사해놔야 무한루프에 빠질 위험이 줄어듦
- 주로 백트래킹과 함께 쓰여, 모든 노드를 다 방문하는 것을 차단함

* * *

### 📕풀이방향
[내 포스팅 : [Python/파이썬] [🥈3] 백준 알고리즘 2606 - 바이러스](https://velog.io/@keynene/Python%ED%8C%8C%EC%9D%B4%EC%8D%AC-3-%EB%B0%B1%EC%A4%80-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-2606-%EB%B0%94%EC%9D%B4%EB%9F%AC%EC%8A%A4)
*이 포스팅을 마지막으로 **정석 DFS 알고리즘 풀이**는 마무리하려고 한다
 ```(dy, dx라는 좋은 DFS알고리즘 풀이를 이제서야 이해했기 때문...🤦🏻‍♀️)```
 
우선 입력값 m,n,k와 주어지는 노드들을 저장하자
노드들을 이용해 ```for loof```으로 모눈종이를 **MAP**영역을 색칠하고, 
완성된 MAP을 이용해 ```dfs()```를 반복호출하며 
<span style="color:red">색칠되지 않은</span> 영역의 개수 ```(cnt)```와 영역의 넓이```(dep)```를 반환하여 출력하자

* * *

### 📝알고리즘 구현순서
1. m,n,k와 주어지는 노드들을 node(list)에 저장하고, amap(map)을 n*m크기로 초기화하자
2. 노드들은 start point와 end point로 주어지는데, ```[[sx,sy,ex,ey], ...]```형태로 저장해두고, 
 ```for loof```를 sx→ex까지, sy→ey까지 반복하면서 모눈종이를 "1"로 색칠하자
 : 또한, 문제에서 주어진 그림과 실제 컴퓨터에서 그려지는 그림은 상하반전임!
3. ```for loof```을 이용하여 amap[y][x]이 0이면 ```dfs(x,y)```를 호출하면서
  함수안에서 <span style="color:red">색칠되지 않은</span> 영역의 넓이```(dep)```을 계산하여, ```res```에 저장하고,
  <span style="color:red">색칠되지 않은</span>  영역의 개수```(cnt)```를 +1 증가시키자
```
    BUT
    성공적으로 구현하여 제출하면 런타임에러 중 (Recursion Error)를 보게되는데,
    이는 백준에서 재귀호출의 깊이를 임의로 "1000"으로 지정해둬서 발생하는 에러이다.
    
    👉🏻해결방법
     imprt sys
     sys.setrecursion(100000)
     sys 라이브러리를 사용하여, 재귀호출의 깊이를 임시크기로 늘리자!
     100000이든, 10000000이든 내 함수의 최대깊이보다 깊으면 된다.
     
     또는
     dx, dy를 이용한 DFS알고리즘을 구현하면 되는데 이는 다음 포스팅에서 다루도록 하겠다.
```
  
* * * 

### 💻결과코드
```python
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

m,n,k = map(int, input().split())
node = [list(map(int,input().split())) for _ in range(k)]
amap = [[0 for _ in range(n)] for _ in range(m)]
cnt = 0   #영역의 개수를 최종반환할 변수
res = []  #영역 당 넓이를 최종반환할 list (sort를 이용하여 오름차순할 예정)

#모눈종이 색칠하기
for sx,sy,ex,ey in node:
    for x in range(sx,ex):
        for y in range(sy,ey):
            amap[y][x] = 1

#색칠안된 영역의 넓이 구하면서 색칠해주기 (재방문하지 않게 하려고 색칠)
def dfs(x,y):
    global dep
    if x<0 or y<0 or x>=n or y>=m:
        return
    if amap[y][x]:  
        return
    else:  
        dep += 1   #현재 영역의 넓이를 저장(global이므로 함수 밖으로 전달 가능) 
        amap[y][x] = 1  
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
    return

#색칠안된 영역 넓이, 개수 구하기
for y in range(m):
    for x in range(n):
        if not amap[y][x]:
            dep = 0
            dfs(x,y)
            res.append(dep)
            cnt += 1  #영역의 개수를 저장함
print(cnt)
print(*sorted(res))
```

* * *

#### ✏️1. n, m, node 입력받으면서 amap 초기화
```python
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

m,n,k = map(int, input().split())
node = [list(map(int,input().split())) for _ in range(k)]
amap = [[0 for _ in range(n)] for _ in range(m)]
cnt = 0   #색칠안된 영역의 개수를 최종반환할 변수
res = []  #색칠안된 영역 당 넓이를 최종반환할 변수 (오름차순 할 예정)
```

* * *

#### ✏️2. node(list)를 이용하여 amap 모눈종이 색칠하기
```python
#모눈종이 색칠하기
for sx,sy,ex,ey in node:
    for x in range(sx,ex):
        for y in range(sy,ey):
            amap[y][x] = 1
```
```
❓동작원리

1.번에서 이미 node에 [[sx,sy,ex,ey] ...]형태로 저장해뒀다
그 node를 하나씩 꺼내면서 x값은 sx→ex만큼, y값은 sy→ey만큼 색칠한다.

※ex, ey값은 이미 1씩 더해져 있으므로 -1해줄 필요가 없다.
  (sx=2, ex=4이면 2,3이 색칠된다)
```

* * *

#### ✏️3. dfs(x,y)를 이용하여 색칠 안 된 영역 크기/개수 구하기
```python
#색칠안된 영역의 넓이 구하면서 색칠해주기 (재방문하지 않게 하려고 색칠)
def dfs(x,y):
    global dep
    if x<0 or y<0 or x>=n or y>=m:  #주어진 영역 벗어나면 return
        return
    if amap[y][x]:  #현재 amap이 1, 즉 색칠되어 있으면 return
        return      #(색칠 안 된 영역을 구할꺼니까)
    else:           #현재 amap이 0, 색칠되어 있지 않으면
        dep += 1    #넓이 증가
        amap[y][x] = 1  #현 amap재방문하지 않도록 1로 색칠
        dfs(x-1,y)     #4방향으로 dfs 재호출
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
    return
    
#색칠안된 영역 넓이, 개수 구하기
for y in range(m):
    for x in range(n):
        if not amap[y][x]:  #amap이 현재 색칠이 안 되어 있으면
            dep = 0
            dfs(x,y)	    #dfs()에 x,y값 전달
            res.append(dep) #dfs()에서 저장한 dep값 res에 저장
            cnt += 1        #dfs()가 한 번 동작했으므로 cnt+1
print(cnt)
print(*sorted(res))   #print의 "*"요소는 list의 "[]"를 떼고 출력해준다
```

* * *

### 📚정리

[내 포스팅 : [Python/파이썬] [🥈3] 백준 알고리즘 2606 - 바이러스](https://velog.io/@keynene/Python%ED%8C%8C%EC%9D%B4%EC%8D%AC-3-%EB%B0%B1%EC%A4%80-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-2606-%EB%B0%94%EC%9D%B4%EB%9F%AC%EC%8A%A4)
[내 포스팅 : [Python/파이썬] [🥈2] 백준 알고리즘 11724 - 연결 요소의 개수](https://velog.io/@keynene/Python%ED%8C%8C%EC%9D%B4%EC%8D%AC-2-%EB%B0%B1%EC%A4%80-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-11724-%EC%97%B0%EA%B2%B0-%EC%9A%94%EC%86%8C%EC%9D%98-%EA%B0%9C%EC%88%98)
[현재 포스팅 : [Python/파이썬] [🥈1] 백준 알고리즘 2583 - 영역 구하기](https://velog.io/@keynene/Python%ED%8C%8C%EC%9D%B4%EC%8D%AC-1-%EB%B0%B1%EC%A4%80-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-2583-%EC%98%81%EC%97%AD-%EA%B5%AC%ED%95%98%EA%B8%B0)
외,
[백준 DFS문제 모음](https://www.acmicpc.net/workbook/view/1063) 에서 "연결 요소의 개수"부터 현 문제 "영역구하기" 까지 
**정석 DFS알고리즘**으로 풀어보았다.
(dfs(x,y)를 4방향(x-1,y), (x+1,y), (x,y-1), (x,y+1)으로 재귀호출하면서 푸는 방식)

이제 **정석 DFS알고리즘**방식은 충분히 연습한 것 같으니,
**dx[-1,1,0,0], dy[0,0,-1,1]**과 같이 좌표를 이용한 **DFS알고리즘** 풀이를 연습하려 한다.

```그렇다고 dx,dy를 이용한 DFS가 정석알고리즘이 아니라는 건 아님....```