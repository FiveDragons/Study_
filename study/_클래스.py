# 클래스 : 반복되는 변수 & 메서드(함수)를 미리 정해놓은 틀(설계도)


# 클래스는 왜 필요한가?
'''
result = 0      # 전역변수
def add(num):   # add(num) 함수를 호출할 경우
    global result   # global을 사용하여 전역변수에 영향을 끼침
    result += num   # 전역변수에 있는 result에 num을 더한다.
    return result   # result에 num을 더한 값을 return해준다.
print(add(3))   # 이렇게 하나를 계산을 할땐 클래스가 필요 없다.
print(add(4))
'''

# 클래스를 쓰는 방법

class Calculator:          # Class를 입력하고 대문자로 시작하는 클래스의 이름을 작성
    def __init__(self):    # 안에 들어갈 함수와 변수를 설정 
        self.result = 0    
    def add(self, num):
        self.result += num
        return self.result
cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))