# [Silver V] 덩치 - 7568 

[문제 링크](https://www.acmicpc.net/problem/7568) 

### 성능 요약

메모리: 30840 KB, 시간: 68 ms

### 분류

브루트포스 알고리즘(bruteforcing), 구현(implementation)

### 문제 설명

<p>우리는 사람의 덩치를 키와 몸무게, 이 두 개의 값으로 표현하여 그 등수를 매겨보려고 한다. 어떤 사람의 몸무게가 x kg이고 키가 y cm라면 이 사람의 덩치는 (x, y)로 표시된다. 두 사람 A 와 B의 덩치가 각각 (x, y), (p, q)라고 할 때 x > p 그리고 y > q 이라면 우리는 A의 덩치가 B의 덩치보다 "더 크다"고 말한다. 예를 들어 어떤 A, B 두 사람의 덩치가 각각 (56, 177), (45, 165) 라고 한다면 A의 덩치가 B보다 큰 셈이 된다. 그런데 서로 다른 덩치끼리 크기를 정할 수 없는 경우도 있다. 예를 들어 두 사람 C와 D의 덩치가 각각 (45, 181), (55, 173)이라면 몸무게는 D가 C보다 더 무겁고, 키는 C가 더 크므로, "덩치"로만 볼 때 C와 D는 누구도 상대방보다 더 크다고 말할 수 없다.</p>

<p>N명의 집단에서 각 사람의 덩치 등수는 자신보다 더 "큰 덩치"의 사람의 수로 정해진다. 만일 자신보다 더 큰 덩치의 사람이 k명이라면 그 사람의 덩치 등수는 k+1이 된다. 이렇게 등수를 결정하면 같은 덩치 등수를 가진 사람은 여러 명도 가능하다. 아래는 5명으로 이루어진 집단에서 각 사람의 덩치와 그 등수가 표시된 표이다.</p>

<table class="table table-bordered" style="width: 35%;">
	<thead>
		<tr>
			<th style="text-align: center;">이름</th>
			<th style="text-align: center;">(몸무게, 키)</th>
			<th style="text-align: center;">덩치 등수</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="text-align: center;">A</td>
			<td style="text-align: center;">(55, 185)</td>
			<td style="text-align: center;">2</td>
		</tr>
		<tr>
			<td style="text-align: center;">B</td>
			<td style="text-align: center;">(58, 183)</td>
			<td style="text-align: center;">2</td>
		</tr>
		<tr>
			<td style="text-align: center;">C</td>
			<td style="text-align: center;">(88, 186)</td>
			<td style="text-align: center;">1</td>
		</tr>
		<tr>
			<td style="text-align: center;">D</td>
			<td style="text-align: center;">(60, 175)</td>
			<td style="text-align: center;">2</td>
		</tr>
		<tr>
			<td style="text-align: center;">E</td>
			<td style="text-align: center;">(46, 155)</td>
			<td style="text-align: center;">5</td>
		</tr>
	</tbody>
</table>

<p>위 표에서 C보다 더 큰 덩치의 사람이 없으므로 C는 1등이 된다. 그리고 A, B, D 각각의 덩치보다 큰 사람은 C뿐이므로 이들은 모두 2등이 된다. 그리고 E보다 큰 덩치는 A, B, C, D 이렇게 4명이므로 E의 덩치는 5등이 된다. 위 경우에 3등과 4등은 존재하지 않는다. 여러분은 학생 N명의 몸무게와 키가 담긴 입력을 읽어서 각 사람의 덩치 등수를 계산하여 출력해야 한다.</p>

### 입력 

 <p>첫 줄에는 전체 사람의 수 N이 주어진다. 그리고 이어지는 N개의 줄에는 각 사람의 몸무게와 키를 나타내는 양의 정수 x와 y가 하나의 공백을 두고 각각 나타난다.</p>

### 출력 

 <p>여러분은 입력에 나열된 사람의 덩치 등수를 구해서 그 순서대로 첫 줄에 출력해야 한다. 단, 각 덩치 등수는 공백문자로 분리되어야 한다.</p>

## 📖[Python/파이썬] [🥈5] 백준 알고리즘 7568 - 덩치
### 📜문제
![](https://velog.velcdn.com/images/keynene/post/be2ab148-283d-4523-bce8-9aed0fdb1b12/image.png)
![](https://velog.velcdn.com/images/keynene/post/2ac1e9cf-1735-4f64-9bdb-b913f16c0bc7/image.png)

* * *

### 📕풀이방향
testcase(tc)를 변수에 저장하고 tc만큼 반복문을 돌려서 몸무게(a),키(b)를 입력받아 person이라는 1차원배열에 [a,b]형식으로 저장해서 2차원배열을 만들자
person[0]인덱스를 person[0~4]를 차례로 2중첩 반복문으로 비교해주자
```
ex)
	 1반복문         2반복문
    person[0] → person[0~4]비교, 
    person[1] → person[0~4]비교 ...
```
2중첩 반복문에서 person[0]이 person[0~4]보다 작으면 횟수마다 등수를 +1 해주고 출력하자

* * *

### 📝알고리즘 구현순서 (브루트포스)
1. testcase(tc)와 person=[] 저장 후, <span style="color:red">person[]에 [a,b]형태로(2차원배열)</span> size입력값 저장
2. 2중첩 for 문으로 비교대상 person[0](ex/ 55,185)를 증가시키며 person[0~4]와 비교,
   person[0]이 person[0~4]보다 a, b값 둘 다 작으면(덩치가 작으면) 등수 +1
   (등수가 높을수록 덩치가 작다는 뜻이니까)
   
* * *

### 💻결과코드
```python
import sys

tc = int(sys.stdin.readline().strip())
person = []

#2차원 배열로 입력값 저장
for _ in range(tc):
    a, b = map(int, sys.stdin.readline().split())
    person.append([a,b]) 
    #[[a1,b1], [a2,b2] ...]

for size in person: #비교대상 : person[0](55,185)
    rank = 1
    for comp in person: #비교할대상 : person[0~4](55,185 ~ 46,155)
        if size[0] < comp[0] and size[1] < comp[1]:
            rank += 1
    print(rank, end=' ')
```

* * *

#### ✏️1. 각 입력값 저장 (person은 2차원배열)
```python
import sys

tc = int(sys.stdin.readline().strip())
person = []

for _ in range(tc):
    a, b = map(int, sys.stdin.readline().split())
    person.append([a,b])
```
```
2차원배열로 초기화/선언/저장 등 방법은 많겠지만,
예제와 같이 비교대상이 "한줄에 한케이스씩" 입력될 경우
person = [] 이라는 빈 list 안에 [a,b]형태로 넣어주는 것이 간단할 것이라고 판단함
(tc를 제일 처음 받기도 했으니까, 반복문을 tc까지 받으면서 입력받음)
```

* * *

#### ✏️2. 2중첩반복문 돌리면서 덩치값 비교
```python
#비교대상 person[0]
for size in person:
    rank = 1
    
    #비교할대상 person[0~4]
    for comp in person:
        if size[0] < comp[0] and size[1] < comp[1]:
            rank += 1
    print(rank, end=' ')
```
```
※덩치가 작은순에서 등수를 +1 할 생각을 하지말고, 제일 크다고 가정하고 -1 씩 계산하면 편함

1. 우선 모든 사람들 덩치값을 rank=1로 고정
   : 반복문을 돌면서 비교대상이 덩치가 작은 경우가 아니라면 (if True가 아니라면) 1등이니까 
2. 덩치를 비교하면서 size[0](몸무게) 와 size[1](키) 둘 다 작으면 rank+1
   : 비교대상이 비교하는대상보다 덩치가 작으면 2등, 3등, 4등 ... 등수가 낮아지니까
```

* * *

### 📚기존 내 알고리즘의 오류와 정리

1. <code>sort()</code>로 대상들을 오름차순 정렬해놓고 순서대로 등수를 출력하려고 했음
❌ 몸무게는 작고 키는 큰 경우도 등수를 체크해버려서 오류 발생
2. <code>sort()</code> 후 키를 비교하면서 키까지 작으면 등수를 -1 하려고 했음
❌ 키를 비교하는 반복문, 몸무게를 비교하는 반복문 늘어나면서 복잡해짐

🤦🏻‍♀️왜 <code>sort()</code>에 집착했을까?
  그냥 전케이스 비교(브루트포스)와 동시에 등수를 계산하면 편할 것을...
  
* * *
  
#### ※2차원배열 for문 탐색과정
이건 내 스스로 자꾸 헷갈려서 하는 정리..
```python
imoprt sys

person = [[a, b], [c, d]]

for i in person:
  print(i)  #결과 [a, b]\n [c, d]
  print(person)  #결과 [[a, b], [c, d]]\n [[a, b], [c, d]]
```
```
1. for i in person > i
   : person 안에 들어가 있는 요소를 하나씩 반환함 
     (person의 크기만큼 0~n까지의 요소를 반환)
   : person[0] = [a,b]  /  person[1] = [c,d] 이므로
   
2. for i in person > person
   : person list 자체를 person의 크기만큼 반환함
   : person = [[a, b], [c, d]] 이므로 [[a, b], [c, d]]\n [[a, b], [c, d]]
```
학과 과정에서 C언어로 처음 코딩을 배웠다보니, for in 문이 어색하다
for()문은 일반적으로 i라는 변수를 배열의 index값으로 사용하다보니,
for i in person > i는 "0,1,2,3..."일 것이라는 고정관념이 부른 오류...


#### 👉🏻 for in 반복문에서 변수(일반적으로 i)값은 </br>배열의 한 <span style="color:red">요소</span>를 순서대로 출력해준다는 것을 까먹지 말자
```
2차원 배열에서 1중첩 반복문의 i값은 2차원 배열의 한 요소(줄)을 의미한다
(위 person에서는 [a,b]와 [c,d]를 의미)
만약 위 예제에서 a, b, c, d 이렇게 꺼내고 싶다면 2중첩 배열의 변수값을 호출해야 한다
```
   ```python
   for i in person:
   	print(i) #[a,b]\n [c,d]
   
   for i in person:
   	for j in i: #i=0 → [a,b]에서의 요소를 호출, i=1 → [c,d]에서의 요소를 호출
   		print(j)  #결과 a\n b\n c\n d 
   ```
   이만하면 좀 이해하고 외우자,..