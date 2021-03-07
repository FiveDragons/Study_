# if문 
# 다른 프로그램과 달리 들여쓰기를 맞추지 않으면 오류가 난다 (Tap을 잘 할 것)

# = 와 == 를 구분을 잘 해야한다. 
# =   :  오른쪽에 있는 것을 왼쪽에 넣는다 ( a = 5 : a에 5를 넣는다. )
# ==  :  오른쪽과 왼쪽이 같다. (a == b : a와 b는 같다.)

# 파이썬 불리언의 특이점

# "Python"  =>   참             [문자열 자료형 / 값이 있다면 = 참]
# ""        =>   거짓           [문자열 자료형 / 값이 없다면 = 거짓]
# [1,2,3]   =>   참             [리스트 / 값이 있다면 = 참]
# []        =>   거짓           [리스트 / 값이 없다면 = 거짓]
# ()        =>   거짓           [튜플 / 값이 없다면 = 거짓]
# {}        =>   거짓           [딕셔너리 / 값이 없다면 = 거짓]
# 1         =>   참             [숫자1 = 참]
# 0         =>   거짓           [숫자0 = 거짓]
# None      =>   거짓           [None == Null / 아무 값이 없음 = 거짓]

'''
# if문은 불리언 자료형으로 실행할지 안할지 결정이 나기 때문에 연산자를 이용하여 불리언을 만들 수 있다.
# [x < y]  =>  [x가  y보다 작다]  :  (True)
# [x != y]  =>  [x와 y가 같지 않다.]  :  (True)

x = 0
y = 1
if x < y:  # x가 y보다 작다면 True,
    print("True : x가  y보다 작다")  # if 조건식이 True일 경우 if문 출력
else:      # x가 y보다 크다면 위의 식이 틀력으니 else 실행
    print("False : x가  y보다 크다") # if 조건식이 False일 경우 else문 출력
'''


'''
# if문 쓰는 법

money = True    
if money:                    # 돈이 있다면(True)
    print("택시를 타고 가라") # "택시를 타고 가라"를 print
else:                        # 돈이 없다면(False)
    print("걸어 가라")        # "걸어 가라"를 print
'''

'''
# or(|) : 둘 중 하나라도 True라면 True이다.
money = 2000
card = 1
if money >= 3000 or card: # money >= 3000는 "False" / card는 "True" (즉, False or True)
    print("or의 결과 : True")

# and(&) : 둘 다 True라면 True이다.
if money == 2000 and card: # money == 2000는 "True" / card는 "True" (즉, True or True)
    print("and의 결과 : True")

# in : in 오른쪽에 리스트, 튜플 등을 놓고 왼쪽의 값이 오른쪽 리스트, 튜플등에 있는 것인지 묻는다.
if 1 in [1,2,3]: # list 안에 1이 들어있어서 True
    print("in의 결과 : True")

# not : 반대를 의미한다.
if not False: # False의 반대인 True가 된다.
    print("not의 결과 : True")

'''

'''
# pass : 조건문에서 아무 일도 하지 않게 설정한다.
a = True
if a:       # a는 True이기에 실행
    pass    # 실행을 했지만 pass이기에 아무일도 일어나지 않는다.
'''

'''
# 다중 if문 : if문의 식이 True가 아니라면 elif로 내려가서 다시 실행 (반복) 결국 모든게 다 아니라면 else 실행
pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket: # pocket안에 money가 있을 경우 실행
    print("pocket 안에 money 있음") 
elif card: # 위 if문 식이 False일 경우 실행 / card가 있을경우 실행
    print("card 보유중")
else: # 위 if, elif문 식이 전부 False일 경우 실행
    print("보유한 것이 없음")
'''

'''
# 조건부 표현식

# 식 1
score = 70
if score >= 60: # score는 70이기에 True이다.
    message = "success"
else:
    message = "failure"
print(message) # if문이 Ture이기 때문에 변수 message에 success가 담긴다.

# 식 2 (파이썬의 3항 연산자)
score = 70
message = "success" if score >= 60 else "failure"
print(message)

# [식 1] 과 [식 2]의 값은 같지만 더 간단하게 작성할 수 있는건 [식 2]의 방식 이다.
'''