# 내장함수 : 파이썬에서 기본적으로 포함하고 있는 함수로 print처럼 기본적으로 사용할 수 있는 함수이다.
# ex ) print(), type()


'''
# abs : 절대값
print(abs(3))
print(abs(-3))    # 절대값(abs)으로 인해 -3이 3으로 출력됨
print(abs(-1.2))  # 절대값(abs)으로 인해 -1.2이 1.2으로 출력됨
'''

'''
# all : 모두 참인지 검사
print(all([1,2,3]))     
print(all([1,2,3,0]))   # 정수는 0을 False로 인식하기에 False로 출력
'''
'''
# any : 하나라도 참이 있는가?
print(any([1,2,3,0]))  
print(any([0, ""]))  
'''

'''
# chr : ASCII 코드를 입력받아 문자 출력
print(chr(97))  # 97번 아스키코드를 출력함
print(chr(48))  # 48번 아스키코드를 출력함
'''

'''
# dir : 자체적으로 가지고 있는 변수나 함수를 보여줌
print(dir([1,2,3]))     # 쓸 수 있는 명령어를 보여줌
print(dir({'1':'a'}))
'''

'''
# divmod : 몫과 나머지를 튜플 형태로 돌려줌
print(divmod(7, 3))     # 7과 3의 (몫, 나머지) 값을 튜플로 나타냄
print(divmod(1.3, 0.2))
'''

'''
# enumerate : 어떠한 리스트가 있다면 딕셔너리처럼 빼서 쓸 수 있게 함
for i, name in enumerate(['body', 'foo', 'bar']): #
    print(name, i)
'''

'''
# eval : 실행 후 결과값을 돌려줌
print(eval('1+2'))
print(eval("'hi' + 'a'"))
'''

'''
# filter : 함수를 통과하여 참인 것만 돌려줌
def positive(x):
    return x > 0
a = list(filter(positive,[1, -3, 2, 0, -5, 6]))
print(a)

# 위 함수와 같음
a = list(filter(lambda x: x > 0, [1, -3, 2, 0, -5, 6]))
print(a)
'''

'''
# len : 길이
print(len("python"))
print(len([1,2,3]))
'''

'''
# map : 각 요소가 수행한 결과를 돌려줌
def tow_times(x): 
    return x*2
a = list(map(tow_times, [1,2,3,4]))
print(a)

a = list(map(lambda a: a*2, [1,2,3,4])) 
print(a)
'''

'''
# max : 최대 값
print(max([1, 2, 3]))
print(max("ㄱㄴㄷ")) # 문자열: A,ㄱ 가 가장 낮고 / Z,ㅎ 이 제일 높다.
# min : 최소 값
print(min([1, 2, 3]))
print(min("python"))
'''

'''
# open : 열고 쓰고 추가하고

# 파일 열기모드     |        설명

#     w(Write)     |     쓰기모드 - 파일에 내용을 쓸 때 사용 (갈아엎기)
#     r(read)      |     읽기모드 - 파일을 읽기만 할 때 사용 (불러오기)
#     a(add)       |     추가모드 - 파일의 마지막에 새로운 내용을 추가 시킬 때 사용 (추가하기)
'''

'''
# pow : 제곱한 결과값 반환(**)
print(pow(2, 4))
print(pow(3, 3))
'''

'''
# range : 0번 index ~ ..번 index
print(list(range(5)))
print(list(range(5, 10))) # 5~9까지의 수를 list로 만들고 그 값을 출력하라.
print(list(range(1, 10, 2))) # 1~10까지의 수에 다다음(2)수들을 list로 만들고 그 값을 출력하라.
'''

'''
# sorted : 정렬
print(sorted([3, 1, 2])) 
print(sorted(['a', 'c', 'b']))
print(sorted("zero"))
print(sorted((3, 2, 1)))
'''

'''
# str : 문자열 반환
print(str(3))
print(str('hi'))
print(str('hi'.upper())) # upper : 대문자 변환
'''

'''
# tuple : 튜플 반환
print(tuple("abc"))
print(tuple([1,2,3]))
print(tuple((1,2,3)))
'''

'''
# list : 리스트로 변환
print(list("python"))# "python" 이라는 문자를 list 하나하나로 바꿈
print(list((1,2,3))) # (1,2,3) 튜플을 list로 바꿈

a = [1,2,3]
b = list(a)
print(b)
'''

'''
# type : 타입 출력

print(type("abc"))
print(type([ ]))
print(type(open("test", 'w'))) # open함수
'''

'''
# zip : 자료형을 묶어주는 역할
print(list(zip([1,2,3], [4,5,6]))) # 첫번째 list와 두번째 list의 0번 index끼리 튜플로 합치고 그 튜플들을 list에 담는다. 
print(list(zip([1,2,3],[4,5,6],[7,8,9])))
print(list(zip("abc", "def")))
'''
