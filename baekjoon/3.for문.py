# for i in range(1,10):
#    print(i)

# 김용오는 이 식을 제대로 알고 공부하길 바란다. 





# 문제 : N을 입력받은 뒤, 구구단 N단을 출력하는 프로그램을 작성하시오. 출력 형식에 맞춰서 출력하면 된다.

# 입력 : 첫째 줄에 N이 주어진다. N은 1보다 크거나 같고, 9보다 작거나 같다.

# 출력 : 출력형식과 같게 N*1부터 N*9까지 출력한다.
'''
# 풀이

N = int(input())

cut = 1
for i in range(9):
    N * cut
    print(N, "*", cut, "=", N * cut)
    cut += 1
'''





# 문제 : 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

# 입력 : 첫째 줄에 테스트 케이스의 개수 T가 주어진다.
#        각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)

# 출력 : 각 테스트 케이스마다 A+B를 출력한다.

# 풀이
'''
# T = int(input())

# for i in range(T):
#     A, B = map(int, input().split())
#     print(A+B)
'''
# 문제를 잘못 파악하였다. 이렇게 쉽게도 가능한 것이었지만 난 input을 전부 입력하면 원하는 값이 나중에 쭉 나와야하는줄 알고 있었다.

'''
# T = int(input())

# L = []
# C = 0

# for i in range(T):
#     A, B = map(int, input().split())
#     L.append(A+B)
    
# for i in range(T):
#     print(L.pop(C))
'''
# 이건 내가 잘못 이해하고 최초로 풀어본 답이다. 
# []없이 답을 추출하려고 하다보니 pop을 사용하였다.

'''
T = int(input())

L = []

for i in range(T):
    A, B = map(int, input().split())
    L.append(A+B)
    
for i in L:
    print(i)
'''
# 이건 다른사람이 푼걸 참고한 것이다.
# 코드가 더 간결해지고 이해하기도 더 쉽다.





# 문제 : n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.

# 입력 : 첫째 줄에 n (1 ≤ n ≤ 10,000)이 주어진다.

# 출력 : 1부터 n까지 합을 출력한다.

# 풀이
'''
n = int(input())
num = 0

for i in range(n+1):
    num += i

print(num)
'''





# 문제 : 본격적으로 for문 문제를 풀기 전에 주의해야 할 점이 있다. 입출력 방식이 느리면 여러 줄을 입력받거나 출력할 때 시간초과가 날 수 있다는 점이다.
#        Python을 사용하고 있다면, input 대신 sys.stdin.readline을 사용할 수 있다. 
#        단, 이때는 맨 끝의 개행문자까지 같이 입력받기 때문에 문자열을 저장하고 싶을 경우 .rstrip()을 추가로 해 주는 것이 좋다.

# 입력 : 첫 줄에 테스트케이스의 개수 T가 주어진다. T는 최대 1,000,000이다. 다음 T줄에는 각각 두 정수 A와 B가 주어진다. A와 B는 1 이상, 1,000 이하이다.

# 출력 : 각 테스트케이스마다 A+B를 한 줄에 하나씩 순서대로 출력한다.

# 풀이
'''
import sys

T = int(sys.stdin.readline().rstrip())

for i in range(T):
    A, B = map(int, sys.stdin.readline().split())
    print(A+B)
'''
# sys 모듈은 python 인터프리터가 제공하는 변수와 함수를 직접 제어할 수 있게 해주는 모듈이다.
# sys.stdin : 모든 대화식 입력에 사용됨 ( input() 호출을 포함 )
# readline() : 파일의 내용을 한 행씩 읽는다.
# lstrip, rstrip, strip 함수는, 순서대로 왼쪽, 오른쪽, 양쪽 문자열 끝의 공백을 지워줍니다.





# 문제 : 자연수 N이 주어졌을 때, 1부터 N까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.

# 입력 : 첫째 줄에 100,000보다 작거나 같은 자연수 N이 주어진다.

# 출력 : 첫째 줄부터 N번째 줄 까지 차례대로 출력한다.

# 풀이
'''
N = int(input())

for i in range(1,N+1):
    print(i)
'''




# 문제 : 자연수 N이 주어졌을 때, 1부터 N까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.

# 입력 : 첫째 줄에 100,000보다 작거나 같은 자연수 N이 주어진다.

# 출력 : 첫째 줄부터 N번째 줄 까지 차례대로 출력한다.

# 풀이

'''
N = int(input())
num = N
for i in range(1,N+1):
    print(num)
    num -=1
'''
# 난 이렇게 풀었지만 쉬운 방법이 당연히 있을 것 같아서 찾아보았다.

'''
N = int(input())

for i in range(N, 0, -1):
    print(i)
'''
# range함수의 괄호 안에 세 개의 숫자를 사용했는데 숫자가 세 개인 경우에는 차례대로 range(start, stop, step)을 의미한다
# 진짜 쉽다.
'''
n = int(input())
for i in range(1, n+1)[::-1]:
    print(i)
'''
# range 함수를 쓸 때는 1부터 n까지의 숫자 범위를 생성하고 인덱스의 범위 연산자 [::-1]를 이용해서 역순으로 값이 출력되도록 하였다. 





# 문제 : 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

# 입력 : 첫째 줄에 테스트 케이스의 개수 T가 주어진다.
#        각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)

# 출력 : 각 테스트 케이스마다 "Case #x: "를 출력한 다음, A+B를 출력한다. 테스트 케이스 번호는 1부터 시작한다.

# 풀이 [1]
'''
T = int(input())
x = 1

for i in range(T):
    A, B = map(int, input().split())
    print('Case #'+ str(x) +': '+ str(A+B))
    x += 1
'''
# 정답은 맞지만 다른 사람걸 참고하니 시간단축에 신경쓴게 보였다.

# 풀이 [2]
'''
import sys
num=int(input())
for i in range(num):
    a,b=map(int, sys.stdin.readline().split())
    print("Case #%d: %d" %(i+1,a+b))
'''
# sys 모듈의 sys.stdin.readline()를 이용하여 시간을 절약하였다.

# 또한 [1]처럼 사용하는 것 보단 [2] 처럼 사용하는게 시간이 더 절약된다고 하였다.
# 나도 다음 문제부턴 시간 절약하는 생각을 하며 문제를 풀어봐야겠다.

# [1]
# for i in range(1,num+1):
#     print(i)

# [2]
# for i in range(num):
#     print(i+1)





# 문제 : 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

# 입력 : 첫째 줄에 테스트 케이스의 개수 T가 주어진다.
#        각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)

# 출력 : 각 테스트 케이스마다 "Case #x: A + B = C" 형식으로 출력한다. x는 테스트 케이스 번호이고 1부터 시작하며, C는 A+B이다.

# 풀이
'''
import sys

T = int(sys.stdin.readline())
x = 1

for i in range(T):
    A, B = map(int, sys.stdin.readline().split())
    
    print("Case #{0}: {1} + {2} = {3}".format(i+1, A, B, A+B))
'''
# input 대신 sys.stdin.readline을 사용할 수 있다. 단, 이때는 맨 끝의 개행문자까지 같이 입력받기 때문에 문자열을 저장하고 싶을 경우 .rstrip()을 추가로 해 주는 것이 좋다.
# lstrip, rstrip, strip 함수는, 순서대로 왼쪽, 오른쪽, 양쪽 문자열 끝의 공백을 지워줍니다.





# 문제 : 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제

# 입력 : 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.

# 출력 : 첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다.

# 풀이
'''
import sys

star = int(input())

for i in range(1,star+1):
    print("*" * i)
'''




# 문제 : 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제
#        하지만, 오른쪽을 기준으로 정렬한 별(예제 참고)을 출력하시오.

# 입력 : 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.

# 출력 : 첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다.

# 풀이[1]
'''
star = int(input())

for i in range(1, star+1):
    print(("*" * i).rjust(star))
'''
# "just라는 정렬" 함수를 사용해서 rjust를 해보니 아주 잘 되었다.

# 풀이[2]
'''
star = int(input())

for i in range(1, star+1):
    print(" " * (star - i), end="") # input값 - i 이기에 갈수록 공백의 수는 1씩 줄어들고
    print("*" * i) # 그냥 i 이기에 공백의 수를 채우는 것 처럼 별의 갯수는 늘어난다.
'''
# 파이썬은 print와 println의 구분이 없기에 end=""를 입력해야 \n이 되지 않는다.





# 문제 : 정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.

# 입력 : 첫째 줄에 N과 X가 주어진다. (1 ≤ N, X ≤ 10,000)
#        둘째 줄에 수열 A를 이루는 정수 N개가 주어진다. 주어지는 정수는 모두 1보다 크거나 같고, 10,000보다 작거나 같은 정수이다.

# 출력 : X보다 작은 수를 입력받은 순서대로 공백으로 구분해 출력한다. X보다 작은 수는 적어도 하나 존재한다.

# 풀이[1]

A = []
N, X = map(int, input().split())   # 첫째 줄 => 정수 N과 정수 X를 먼저 input한다.
A = list(map(int,input().split())) # 둘째 줄 => list와 input을 활용하여 수열을 할 수 있게 만든다.

for i in range(N):                 # N만큼 for문을 돌린다.
    if A[i] < X:                   # 수열 A[i] (A list의 i index)의 크기가 X보다 작다면
        print(A[i], end=' ')       # A list의 i inext를 end=' ' 를 적용시켜 print 하여라