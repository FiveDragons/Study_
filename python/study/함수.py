# 함수

# Immutable : 변하지 않는 자료형 => 정수, 실수, 문자열, 튜플
# Mutable : 변할 수 있는 자료형 => 리스트, 딕셔너리, 집합


'''
# 함수 표현식
# def 함수명(매개변수):     # 매개변수 : input
#     <수행할 문장1>        # function
#     <수행할 문장2>
#     . . .
#     return 리턴 값        # output

def sum(a, b):      # def 라는 함수의 정의를 적고, 함수명(sum)을 적은 뒤, 매개변수 인자(a, b) 2개를 넣는다.
    result = a+b    # result라는 변수에 a+b를 담아서
    return result   # result를 return하여 돌려준다.

print(sum(1,2))     # 함수 호출을 하여 a와b의 값을 1,2로 지정하여 1+2 라는 결과를 받음
'''



# 입력, 출력이 없을 수 있다.
'''
# 입력값(매개변수)이 없는 함수 / pop 함수가 이러하다.
def say():
    return 'Hi'
print(say())
'''
'''
#결과값(return)이 없는 함수 / append 함수가 이러하다.
def sum(a, b):
    print(f"{a},{b}의 합은{a+b}입니다.")
print(sum(3,4)) 
'''
'''
# 입력값, 결과값도 없는 함수 / 어디에 사용하는거지..?
def say():
    print('Hi')
print(say())
'''
'''
# 여러 개의 입력값(*args : arguments) : 리스트, 튜플이라 생각하면 쉽다.
def sum_many(*args):  # *args를 사용하면 입력값이 몇개가 되든 상관없이 호출이 잘 된다.
    sum = 0
    for i in args:    # args가 list처럼 입력한 값 순서대로 반복문을 실행한다.
        sum = sum+i
    return sum
print(sum_many(1,2,3,4))
'''
'''
# 키워드 파라미터(**kwargs : keyward argument) : 딕셔너리라고 생각하면 쉽다.
def print_kwargs(**kwargs):   # 
    for k in kwargs.keys():
        if(k == "name"):
            print("당신의 이름은 : " + k)
print(print_kwargs(name="int 조수", b="2"))
'''

'''
# 함수의 결과값은 언제나 하나이다
def sum_and_mul(a,b):
    return a+b, a*b, a-b # 각각의 값이 튜플 형태에 담겨 하나의 값으로 출력된다.

print(sum_and_mul(1,2)[0]) # 난 "더한값만 출력할래" 라는 경우엔 [0]을 사용하여 빼오면 된다.
'''

'''
# 매개변수에 초깃값 미리 설정하기(True)
def say_myself(name, old, man=True):    # True라고 입력 한다면 초기값을 미리 설정해 놓을 수 있다.
    print(f"나의 이름은 {name} 입니다.")
    print(f"나이는 {old}살입니다.")
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")
say_myself("김용오",25)         # 평소였다면 인자가 부족하다는 에러가 났겠지만 man을 True로 설정해 놨기에 오류없이 출력이 된다.
'''
'''
# 함수 매개변수에 초깃값을 설정할 때 주의할 사항
def say_myself(name, man=True, old):    # True가 적용되어 있는 man이 2번째 인자로 들어간 경우
    print(f"나의 이름은 {name} 입니다.")
    print(f"나이는 {old}살입니다.")
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")
say_myself("김용오", 25)      # 출력시 25를 두번째 인자로 인식하여 오류가나기에 초깃값을 설정한 man을 마지막 인자로 사용하여야 한다.
'''



'''
# 함수 안에서 선언된 변수의 효력 범위
a = 1
def vartest(a):  # 함수 내엔 지역변수라 하여 밖에 있는 전체변수를 가져와 계산만 할뿐
    a += 1      # 전체변수에 영향을 끼치진 못한다.
    
vartest(a) # vartest함수를 사용해 a+1을 해 줬다 생각했지만 함수는 지역변수이기에 아무런 변화가 생기지 않는다.
print(a)
'''
'''
# Mutable : 변할 수 있는 자료형 => 리스트, 딕셔너리, 집합
# 위와 똑같이 전역변수와 지역변수의 b가 다르지만 같은 주소를 사용하기 때문에 append(추가)등을 사용하여 변형을 주어 조작을 할 수 있다.
b = [1,2,3]
def vartest2(b):
    b = b.append(4)
vartest2(b)
print(b)

# Immutable : 변하지 않는 자료형 => 정수, 실수, 문자열, 튜플
# a값에 변형을 할 수가 없기때문에 a에 값을 조작할 수 없다.
a = 1
def vartest(a):  
    a += 1      
vartest(a) 
print(a)
'''
'''
# [1] 전체변수에 영향을 주기위한 방법 : return
a = 1
def vartest(a):  
    a += 1 
    return a    # 리턴을 하여 a에 값이 변할 수 있도록 한다.
    
a = vartest(a)  # 리턴된 a값(a += 1)을 a에 넣는다.
print("값은 : ", a) # 전체변수 a의 값이 변한걸 확인할 수 있다.
'''
'''
# [2] 전체변수에 영향을 주기위한 방법 : global
a = 1
def vartest():  
    global a  # global을 사용하여 전체변수인 a에 영향을 끼칠 수 있다는 뜻이다.
    a += 1 
    
vartest() 
print("값은 : ", a) # 전체변수 a의 값이 변한걸 확인할 수 있다.
'''

'''
# Lambda : 함수를 간단하게 표현하는 방법
def add(a,b):       # 평소에 사용하던 함수방식
    return a+b      
print(add(1,2))

add = lambda a,b: a+b # 2줄로 작성하던걸 1줄로 축약 가능
print(add(1,2))
'''
'''
# Lambda를 사용하면 list에 함수자체를 넣어 사용하는 것도 가능하다.
myList = [lambda a,b: a+b, lambda a,b: a*b]
print(myList[0](1,2)) # myList라는 list안에 0번index인 함수에 a=1, b=2를 설정하여 a+b를 출력하라
'''