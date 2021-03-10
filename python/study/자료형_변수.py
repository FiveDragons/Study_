# 자료형

# 자료에 대한 타입 : 숫자, 문자, 불리언
# 어떤 값을 담는 자료구조 : 변수, 리스트, 튜플, 딕셔너리, 집합

# 자료형은 자료형의 종류에 따라 결과값이 달라진다
# 숫자라면  1  +  1  =  2
# 문자라면 '1' + '1' = '11'

# 수학의 수식과는 차이가 있다
# a = a + 1  : a + 1을  a라는 값에 담는다.

# 변수란 : 어떤 값을 담는 상자이다.
'''
a = 3 
a = a + 1
print(a)
'''



# [추가내용 - 이해가 되지 않는다면 나중에 다시 읽기]
# 변수를 좀 더 내부적으로 보면 "값(객체)은 메모리 안에 있고" 
# "변수는 값(객체)이 들어있는 메모리 안에 주소를 가르키는 역할을 한다."
'''
# [1]
a = [1,2,3]   # a는 [1,2,3]을 담고있는 메모리의 주소를 가르킨다.
b = a         # a는 b에게도 똑같이 그 주소를 가르키게 한다.
a[1] = 4      # a가 가르키는 메모리의 주소에서 1번 index(2)를 4로 바꾸었다.
print(a,b)    # a와 b가 가르키는 주소가 같기에 a와 b의 출력이 같다.
print(id(a))  # id(a)를 이용하여 a가 가르키는 주소를 확인할 수 있다.
print(id(b))  # id(b)를 이용하여 a가 가르키는 주소를 확인할 수 있다.
print(a is b) # a와 b가 같은 주소인지 불리언 값으로 출력해준다.
'''
'''
# [2]
a = [1,2,3]   # a = [1,2,3]을 그대로 b한테 주고싶다면
b = a[:]      # 슬라이싱을 하여 시작부터 끝의 값을 그대로 b에게 준다.             
a[1] = 4      # 이젠 a와 b의 주소가 다르니 a에 들어있는 1번 index만 4로 바뀐다.
print(a,b)    # 아까와 다르게 값이 다르게 출력되는걸 볼 수 있다.

# 정리하자면 b = a 하면 a라는 주소가 넣어진 것이지만
# b = a[:]를 하면 새로운 주소가 따져서 들어간다.
'''
'''
# [3]
from copy import copy # 비슷한 원리를 하나 더 해보자면
a = [1,2,3]
b = copy(a)     # a list 주소를 주는게 아닌 값을 복사하여 b에게 새롭게 할당하겠다.
a[1] = 4
print(a,b)
# 변수의 구조를 내부적으로 시각화 하여 보고싶다면  
# =>http://pythontutor.com/live.html#mode=edit에 들어간 후
# 하단에 render all objects on the heap (Python)로 바꿔준 뒤 위의 식을 입력해보자
'''

# 변수 할당 방법

a = 1   # a에 1을 넣음
print(a)

[a, b] = ['python', 'life'] # a엔 'python' / b엔 'life'를 넣음
print(a)
print(b)

a = b = 'hello' # a, b 변수에 hello라는 값이 담김
print(a is b)

# a, b 변수 값 교환 [1]
a = 3
b = 5
print(a)
print(b)
tmp = b # 임시변수를 만들어 b(5)의 주소를 넣는다.
b = a   # b에 a(3)의 주소를 넣는다.
a = tmp # a에 tmp(5) 주소를 넣는다.
print(a)
print(b)

# a, b 변수 값 교환 [2]
# 파이썬에서만 가능
c = 1
d = 4
c,d = d,c # 보는 그대로 직관적으로 변경 된다.
print("[1 이었던 c의 값은] = ", c)
print("[4 였던 d의 값은] = ", d)





# [ 숫자 ] 

# 정수형
'''
a = 1
print(type(a))
'''
# 실수형
'''
a = 1.5
print(type(a))
'''

# 사칙연산
'''
a = 3
b = 4
# [** : 제곱], [/ : 나누기], [// : 몫], [% : 나머지]
print(a+b, a-b, a*b, a**b, a/b, a//b, a%b, sep="\n")
'''



# [ 문자 ]
'''
a = "Hello world"
print(type(a))
'''
# (이스케이프 문자)
# " ", '', \n, \t
'''
a = 'Python's favorite food is perl'
print(a)
'''
# Syntax error : 프로그래밍 때의 구문의 오류
'''
a = "Python's favorite food is perl" # 반대로 ' '안에 "를 사용해도 문장을 구현할 수 있음
print(a)

a = 'Python\'s favorite food is perl' # \를 사용하면 ', " 등을 문자열로 사용한다고 파이썬에게 알려주는 것
print(a)

a = 'Life is too short \tYou need python' # \t를 이용하면 문자열 사이에 탭 간격을 준다.
a = 'Life is too short \nYou need python' # 파이썬은 한줄씩 읽기에 \n를 사용하여 엔터를 한다.
'''

# """ """, ''' '''

# a = '''Life is too short 
#     You need python'''          # ''', """를 사용하면 이스케이프 문자를 쓰지 않아도 \n기능을 구현할 수 있다.
# print(a)

# 문자열 연결
'''
a = "Python"
b = " is fun!"
print(a+b)
print(a * 100)
'''
# 문자열 자료형
# indexing(인덱싱)
'''
a = 'Life is too short, You need python'
print(a[0])
print(a[-1])
# Slicing(슬라이싱)
# a[이상:미만:간격]
# 비워놓는 경우 맨 처음, 맨 끝 까지
print(a[0:5])
print(a[:5])
print(a[::2])
'''
# 문자열 포매팅
# [%d : 정수]. [%f : 실수], [%s : 문자열]
# %s를 사용하면 웬만한건 다 들어간다. 단 정수와 실수가 문자열로 바뀌니 주의할 것
'''
number = 10
day = "three"
a = "I ate %d apples. so I was sick for %s days." % (number, day)
print(a)
# {} .format
a = "I ate {0} apples. so I was sick for {1} days.".format(number, day)
print(a)
# {변수} .format
a = "I ate {number} apples. so I was sick for {day} days.".format(number = "10", day = "three")
print(a)
# 3.6 이상 버전부터는 f를 앞에만 사용해도 가능하다.
a = f"I ate {number} apples. so I was sick for {day} days."
print(a)
'''
# 정렬과 공백
# %10s(str)를 이용하여 10칸을 뒨다.
'''
a = "%10s" % "hi"
print(a)
# %0.4f(float)를 이용하여 간격.소수점 남기는 자리 수 f
a = "%0.4f" % 3.42134234
print(a)
'''
# 문자열 개수 세기(count)
# a에 있는 hobby에서 b가 몇개있는지 count한다.
'''
a = "hobby"
print(a.count('b'))

# 위치 알려주기1(find)
a = "hobby"
print(a.find('b')) # 있다면 리턴을 하며 index의 자리가 나온다.
print(a.find('x')) # 없는 문자라면 -1이 출력된다.

# 위치 알려주기2(index)
a = "Life is too short"
print(a.index('t')) # 있다면 리턴을 하지만 없다면 에러가 나오기에 find를 사용하는게 더 편하다.

# 문자열 삽입(join)
a = ",".join(['abcd'])
print(a)

a = ",".join(["a","b","c","d"]) # 이와 같이 join은 list에서 자주 사용함
print(a)

# 소문자를 대문자로 바꾸기 (upper)
a = "Hi"
print(a.upper())

# 대문자를 소문자로 바꾸기 (lower)
a = "Hi"
print(a.lower())

# 양쪽 공백 지우기(strip)
a = "  hi  "
print(a.strip()) # 좌우 한쪽의 공백만 지우는 lstrip, rstrip도 있다.

# 문자열 바꾸기(replace)
a = "Life is too short"
print(a.replace("Life", "Your leg")) # Life 라는걸 Your leg로 교체한다.

# 문자열 나누기(split)
a = "Life is too short"
print(a.split()) # 공백을 기준으로 잘라서 리스트로 만든다. (단, (:)안에 무언가 적는다면 공백이아닌 :을 기준으로 잘라서 리스트를 만든다)
'''



