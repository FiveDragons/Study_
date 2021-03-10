# 예외처리 : 오류가 발생했을때 어떻게 할지 정해놓는 것 
# => 오류가 발생하면 프로그램이 다운되기 때문에 그 오류를 어떻게 처리해서 넘어가게끔 만들어서 다운을 막음

# Exception : 하나의 오류를 지목하지 않고 모든 오류를 지목
# elif 처럼 여러개의 오류를 각각 지목하여 예외처리를 할 수 있음

'''
# 사용법

try:
    # 오류가 발생할 수 있는 구문
except Exception as e:
    # 오류 발생
else:
    # 오류 발생하지 않음
finally:
    # "무조건" 마지막에 실행
'''

'''
# 오류 발생시 코드가 종료됨
# ZeroDivisionError라는 에러가 발생하여 print 되지 않고 프로그램이 멈춤

4 / 0
print("오류 확인") 

# 예외처리를 하여 print까지 잘 출력 됨
try:
    4 / 0
except ZeroDivisionError as e:
    print(e) 

print("오류 확인") 
'''

'''
try:
    a = input()
    f = open(a, 'r', encoding='UTF=8') #encoding을 해야 a에 한국어를 넣을 수 있음
except FileNotFoundError as e:
    print(f'open 파일에 {a} 이라는 파일이 없습니다.')
else: 
    pass
'''

'''
# try ... else
try:
    f = open('tryStudy.txt', 'r')  # 파일 오픈
except FileNotFoundError as e:     # 파일이 없다면 
    print(str(e))                  # FileNotFoundError 에러를 출력하라
else:                              # f = open('tryStudy.txt', 'r')에 오류가 없을경우 실행 하여라
    data = f.read()                # 오류가 있기에 실행이 되지 않음.
    print(data)
    f.close()
'''

'''
# try ... finally
f = open('tryStudy.txt', 'w')
try:                    # 오류 날 수 있는 곳에 사용
    data = f.read()
    print(data)
except Exception as e:  # 오류 발생시 예외처리
    print(e)
finally:                # else와 다르게 오류가 나던 안나던 무조건 실행
    f.close()           # 위에 open을 하였으니 무조건 close를 하기위해 사용하는 경우가 많음
'''

'''
# 여러 개의 오류 처리하기
try:
    a = [1,2]
    print(a[3])
    # 4/0
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
except IndexError:
    print("인덱싱할 수 없습니다.")
'''

'''
# 오류회피
try:
    f = open("File", 'r')
except FileNotFoundError:
    pass      # 아무일 없이 그냥 지나감
'''

'''
# 오류 일부러 발생시키기 : raise
class Bird:
    def fly(self): # fly라는 속성을 Bird라는 속성을 오버라이딩 하는 곳에서 다 변형하게 하고싶을 경우 
        raise NotImplementedError # 자식 클래스에서 fly를 변형하지 않은 경우 오류를 내라

class Eagle(Bird):
    pass     # fly를 변형하지 않아 위에 지정한 오류 발생
    # def fly(self):      # fly를 변형함으로써 오류가 발생하지 않았다.
    #     print("very fast")

eagle = Eagle()
eagle.fly()
'''
