# 클래스 : 반복되는 변수 & 메서드(함수)를 미리 정해놓은 틀(설계도)
# 변수와 함수가 똑같은 구조를 계속 여러번 써야되니까 이거는 하나로 묶어서 그냥 설계도를 만들어 보자! 라고 한 것이 클래스 이다.
# 보통 게임 캐릭터를 만들때 사용한다고 생각하면 편하다. (ex : npc)

# 클래스는 과자 틀과 같다. 
# 공장에서 찍어내는 것과 직접 만드는 것의 속도 차이 라고 보면 된다.

# 함수 사용법
'''
result = 0      # 전역변수
def add(num):   # add(num) 함수를 호출할 경우
    global result   # global을 사용하여 전역변수에 영향을 끼침
    result += num   # 전역변수에 있는 result에 num을 더한다.
    return result   # result에 num을 더한 값을 return해준다.
print(add(3))   # 이렇게 하나를 계산을 할땐 클래스가 필요 없다.
print(add(4))
'''

'''
# 클래스를 쓰는 방법

# 1. class를 입력하고
# 2. 대문자로 시작하는 클래스의 이름을 작성
# 3. 안에 들어갈 함수와 변수 설정
class Calculator:          # [1], [2]
    def __init__(self):    # [3]  함수: def / 변수 : result
        self.result = 0    # __init__ : 처음에 클래스가 만들어질때 어떤 값을 설정할지 설정해주는 부분
    def add(self, num):    # add를 이용해서 class를 한번만 정의해 놓으면 계속 찍어낼 수 있다.
        self.result += num # 함수에서 작성했던 것과 비슷하지만 다른점은 class에선 self를 사용한다.
        return self.result # self : class안에있는 함수
cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))
# 이 식에선 더하기만 나왔지만 계산기를 가정하고 봤을때 -,%,/,*등의 연산이 추가로 들어간다면
# 더 복잡해 지니 class로 찍어내기만 하면 된다는 장점이있다.
'''
'''
# [1] 사칙연산 클래스 
class FourCal:  # class를 만드는 기본 설계도를 만들고 이 설계도로 찍어서
    pass
a = FourCal()   # 변수에 넣는다. 그럼 이 변수는 설계도로 만든 과자와 같다.
print(a)        
# <__main__.FourCal object at 0x0000024A682D0DF0> : FourCal이라는 class로 만든 객체이다.
print(type(a))  
# class로 만든 instance
'''

'''
# [2] 사칙연산 클래스
class FourCal:
    def setdata(self, first, second): # 즉, a를 self를 넣어서
        self.first = first            # a의 first라는 변수에 first를 넣는다.
        self.second = second          # a의 second 변수에 second를 넣는다.

a = FourCal()  # FourCal() class를 사용하겠다.
a.setdata(1,2) # a(self) .setdata(함수 사용) (4(first),2(second))
# a라는 과자를 FourCal(self) 라는 공장에 넣어 찍어낸다.

print(a.first)  # 때문에 a.first는 1이라는 수가 들어가고
print(a.second) # a.second는 2라는 수가 들어간다.
'''

'''
# [3] 사칙연산 클래스
class FourCal:
    def setdata(self, first, second): 
        self.first = first            
        self.second = second   
    def add(self):
        result = self.first + self.second
        return result

a = FourCal()    # a라는 변수는 FourCal이라는 기계에 찍어졌다. 때문에 setdata, add 둘 다 사용 가능하다.
a. setdata(4, 2) # setdata함수에 값을 입력한다. (first : 4 / second : 2)
print(a.add())   # add 함수를 활용하여 first값과 second값을 더한뒤 return으로 값을 받는다.
'''

'''
# 생성자(Constructor)
# __이름__은 좀 특별한 기능이 있는 것이다. 어떻게 보면 예약어라고 해서 이거를 쓰면 이런 기능을 해라! 라고 정해놓은 것
# __init__ : class를 시행할때 init이 무조건 처음으로 실행하게 된다.
class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def setdata(self, first, second): 
        self.first = first            
        self.second = second   
    def add(self):
        result = self.first + self.second
        return result

# a = FourCal() # 사칙연산 클래스에선 __init__이 없어 그냥 출력 가능했지만 지금은 오류가 난다.
# 즉, 아래처럼 ()안에 init의 값을 입력해 놔야한다.
a = FourCal(4, 2)
'''

'''
# 클래스의 상속
# 계산기를 예로 들면 class로 계산의 기능을 만들어 놓았고, 추가로 공학용 계산기를 만들고 싶을때
# 공학용 계산기의 기능들을 전부 새로 만들지 않고 계산기 기능을 작성한 class를 상속받아 추가 작성한다.
# 즉, 부모클래스를 상속하여 자식 클래스를 만든다.

class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result

class MoreFourCal(FourCal):  # 부모클래스를 상속 받는 방법 : 괄호 안에 부모클래스의 이름을 적는다.
    pass
# init은 자식클래스에서도 작용한다.

a = MoreFourCal(4, 2) # MorFourCal은 부모클래스를 상속받고 
print(a.add())       # pass만 되어있지만 부모클래스처럼 잘 작동하는걸 볼 수 있다.
#   즉, 상속을 받게 되면 부모의 기능을 모두 쓸 수있다. 
'''

'''
# [2] 클래스의 상속 : 메서드 추가

class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result

class MoreFourCal(FourCal):  # FourCal을 상속받고,
    def pow(self):           # 제곱해주는 함수를 추가로 만듦
        result = self.first ** self.second
        return result

a = MoreFourCal(4,2) # __init__은 없지만 상속을 받았기에 __init__이 있는것 처럼 한다.
print(a.pow())       # pow함수를 활용하여 제곱을 해준다.
'''

'''
# 메서드 오버라이딩
class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

 # 부모클래스를 상속받았으나 div를 수정하였다. 이럴경우에 자식 클래스를 실행하면 수정된 div가 실행된다.
class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second

a = SafeFourCal(4,0)
print(a.div())
'''

'''
# [1]클래스 변수, 객체 변수
class FourCal:
    first = 2   # class변수 : class에 공통적으로 적용되는 변수
    second = 3  
    # def __init__(self, first, second):
    #     self.first = first
    #     self.second = second
    def setdata(self, first, second):  # 객체변수
        self.first = first             
        self.second = second   
    def add(self):
        result = self.first + self.second
        return result
'''
'''
# [2]클래스 변수, 객체 변수
class Family:
    lastname = "김"

Family.lastname = "박" # 설계도 자체를 바꿀 수 있다. : Family라는 설계도를 호출하여 lastname을 수정한다.
print(Family.lastname)

a = Family()
b = Family()
print(a.lastname)
print(b.lastname)
'''