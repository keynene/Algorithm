# [Silver V] 소트인사이드 - 1427 

[문제 링크](https://www.acmicpc.net/problem/1427) 

### 성능 요약

메모리: 113248 KB, 시간: 108 ms

### 분류

정렬(sorting), 문자열(string)

### 문제 설명

<p>배열을 정렬하는 것은 쉽다. 수가 주어지면, 그 수의 각 자리수를 내림차순으로 정렬해보자.</p>

### 입력 

 <p>첫째 줄에 정렬하려고 하는 수 N이 주어진다. N은 1,000,000,000보다 작거나 같은 자연수이다.</p>

### 출력 

 <p>첫째 줄에 자리수를 내림차순으로 정렬한 수를 출력한다.</p>

## 📖[Python/파이썬] [🥈5] 백준 알고리즘 1427 - 소트인사이드
### 📜문제
![](https://velog.velcdn.com/images/keynene/post/c772dd16-5066-4961-b03e-9a28400b2f49/image.png)
![](https://velog.velcdn.com/images/keynene/post/74266119-5419-4ca2-b17f-6c5b474c28e8/image.png)

* * *

### 📕풀이방향
숫자를 순서대로 정렬해야하므로 str()로 받았다가 map()으로 int로 변경하여 list로 저장하자
<code>sort(key=lambda x:-x)</code>를 이용하여 내림차순 정렬하고,
print()의 end=''를 이용하여 공백(\n)없이 출력하자

* * *

### 📝알고리즘 구현순서
1. 입력받음 → str()로 문자로 변경 → map(int,)로 정수으로 변경 → list()로 저장
2. sort의 key를 이용하여 내림차순 정렬
3. print 옵션 이용하여 "\n"떼고 출력

* * *

### 💻결과코드
```python
n = list(map(int,str(input())))
n.sort(key=lambda x:-x)
for i in n:
    print(i,end='')
```