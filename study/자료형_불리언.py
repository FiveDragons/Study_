# 불리언 이란 => True & False : 참 & 거짓
'''
a = True
b = False
print(type(a))
print(type(b))
'''

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
a = "안녕"
if a: # a엔 문자열 자료형이 들어가 있지만 str의 값에 뭔가 있으면 True로 본다.
    print(a) 

b = ""
if b: # a엔 문자열 자료형이 들어가 있지만 str에 값이 없으면 False로 본다.
    print(b) 

c = [1,2,3,4]
if c: # a엔 문자열 자료형이 들어가 있지만 str에 값이 없으면 False로 본다.
    print(c) 
'''

'''
# 응용
c = [1,2,3,4]
while c: # c의 값이 없어질때까지 계속 돈다.(참일경우만 활성화)
    c.pop() # pop : c list의 맨 끝부터 하나씩 빼낸다.
    print(c) 
'''