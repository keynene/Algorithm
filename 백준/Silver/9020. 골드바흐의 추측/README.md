# [Silver II] 골드바흐의 추측 - 9020 

[문제 링크](https://www.acmicpc.net/problem/9020) 

### 성능 요약

메모리: 116760 KB, 시간: 188 ms

### 분류

수학(math), 정수론(number_theory), 소수 판정(primality_test), 에라토스테네스의 체(sieve)

### 문제 설명

<p>1보다 큰 자연수 중에서  1과 자기 자신을 제외한 약수가 없는 자연수를 소수라고 한다. 예를 들어, 5는 1과 5를 제외한 약수가 없기 때문에 소수이다. 하지만, 6은 6 = 2 × 3 이기 때문에 소수가 아니다.</p>

<p>골드바흐의 추측은 유명한 정수론의 미해결 문제로, 2보다 큰 모든 짝수는 두 소수의 합으로 나타낼 수 있다는 것이다. 이러한 수를 골드바흐 수라고 한다. 또, 짝수를 두 소수의 합으로 나타내는 표현을 그 수의 골드바흐 파티션이라고 한다. 예를 들면, 4 = 2 + 2, 6 = 3 + 3, 8 = 3 + 5, 10 = 5 + 5, 12 = 5 + 7, 14 = 3 + 11, 14 = 7 + 7이다. 10000보다 작거나 같은 모든 짝수 n에 대한 골드바흐 파티션은 존재한다.</p>

<p>2보다 큰 짝수 n이 주어졌을 때, n의 골드바흐 파티션을 출력하는 프로그램을 작성하시오. 만약 가능한 n의 골드바흐 파티션이 여러 가지인 경우에는 두 소수의 차이가 가장 작은 것을 출력한다.</p>

### 입력 

 <p>첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고 짝수 n이 주어진다.</p>

### 출력 

 <p>각 테스트 케이스에 대해서 주어진 n의 골드바흐 파티션을 출력한다. 출력하는 소수는 작은 것부터 먼저 출력하며, 공백으로 구분한다.</p>

## 📖[Python/파이썬] [🥈2] 백준 알고리즘 9020 - 골드바흐의 추측
### 📜문제
![](https://velog.velcdn.com/images/keynene/post/dde5802a-2cb2-4d3f-a49d-cae97cb9f1c8/image.png)
![](https://velog.velcdn.com/images/keynene/post/baf9db76-7df4-4e94-8535-d3ca13bad0b6/image.png)

* * *

### 📕풀이방향
N이 2의 배수인데다, N의 범위도 만만해서 2~n까지 2의배수만 모두 소수를 구해 저장해놓고,
abs(절댓값)함수로 N의 소수들을 비교하면서 출력할 생각을 하면 큰 코 다친다...🤦🏻‍♀️

[내 포스팅 : [Python] 백준 알고리즘 4948 - 베르트랑 공준](https://velog.io/@keynene/Python-%EB%B0%B1%EC%A4%80-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-4948-%EB%B2%A0%EB%A5%B4%ED%8A%B8%EB%9E%91-%EA%B3%B5%EC%A4%80)
이전 포스팅에서 위 문제를 해결한 경험으로부터 소수를 리스트에 저장해두는 방법을 떠올려, 
상기 풀이처럼 해결하려고 했으나 또 다시 <span style="color:red">시간초과</span>에 직면했다😭

👉🏻수학적으로 접근하자
n을 입력받되 a,b에 n//2를 각각 저장하여 prime(a)와 prime(b)가 둘 다 소수이면 출력,
소수가 아니면 a--, b++하며 다시 비교하는 방식으로 풀어보자
```a,b 초기값을 n//2으로 지정한 이유 = n이 10인 경우 5,5가 제일 차이가 작으니까```

* * *

### 📝알고리즘 구현순서
1. 소수를 구하는 prime()함수를 만들자
2. t만큼 n을 입력받으며 a,b에 n//2값을 저장하여 prime(a)와 prime(b)가 True이면 출력하자
   (하나라도 False이면 a++, b--)

* * *

### 💻결과코드
```python
import sys
input = sys.stdin.readline

t = int(input().rstrip())

def prime(n):
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

for _ in range(t):
    n = int(input().rstrip())
    a,b = n//2, n//2
    while a > 0:
        if prime(a) and prime(b): #둘 다 True(소수)인 경우
            print(a, b)
            break
        else:
            a -= 1
            b += 1
```
```
❓이 코드가 효율적인 이유

👉🏻 모든케이스의 prime()을 저장하게 만드는게 문제의 함정인데, 
   위 코드는 a,b만 prime()을 호출하여 둘 다 True를 반환할 때만 출력한다.
   (모든케이스를 prime()하면 n번 / a,b만 prime()하면 n/2번만 호출하게됨!)
```

* * *

#### ✏️1. prim() 함수 만들기 (소수이면 True, 아니면 Flase 반환)
```python
import sys
input = sys.stdin.readline

t = int(input().rstrip())

def prime(n):
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
```

* * *

#### ✏️2. n//2를 a,b에 저장하여 prime(a) and prime(b) → true이면 출력
```python
for _ in range(t):
    n = int(input().rstrip())
    a,b = n//2, n//2
    while a > 0:  #a를 a--해가면 결국 0에 도달할 테니까 1이 될 때까지만 실행
        if prime(a) and prime(b): #a,b 다 True이면 출력
            print(a, b)
            break
        else: #하나라도 False이면 a--, b++후 다시 검사
            a -= 1
            b += 1
```

* * *

### 📚초기 알고리즘 오류와 정리
※초기 알고리즘
#### ✍🏻 N의 소수를 다 구하여 절댓값이 최소값이면 출력하기
```python
import sys
input = sys.stdin.readline

t = int(input().rstrip())

def prime(n):
    res = []
    res_prime = ''
    for num in range(n):
        err = 0
        for i in range(2,int(num**0.5)+1):
            if num%i == 0:
                err += 1
        if err == 0:
            res.append(num)
    cnt = max(res)-min(res)
    for a in res:
        for b in res:
            if a+b == n:
                if abs(a-b) < cnt:
                    cnt = abs(a-b)
                    res_prime = str(a)+' '+str(b)
                else:
                    pass
    return res_prime

for _ in range(t):
    n = int(input().rstrip())
    print(prime(n))
```
```
❓내 알고리즘이 틀린 이유

틀리지않았다. 정답이다.
그러나 n이 입력될 때마다 모든 소수를 구하여 list(res)에 저장하고,
res를 다시 절댓값을 비교하면서 prime()안에서 불필요한 for/if문 동작이 많기 때문에
시간초과를 발생시켰다

```

* * *

1. 알고리즘 설계 과정에서 O(N)를 생각하는 것은 이제 당연하다
   '전체 알고리즘이 어떻게 동작할지 / 동작하면서 불필요한 계산은 없는지'
   확인하는 과정이 매우 중요하다
   ```
   어떤 경우는 전체 과정을 다 계산하여 저장하고
   그것을 뽑아 쓰는 것이 효율적인 알고리즘이 되겠지만,
   
   또 어떤 경우는 전체 과정을 다 계산하는 것보다
   필요한 경우만 계산하며 결과를 도출해내는 것이 효율적인 알고리즘이 될 수 있다....
   ```