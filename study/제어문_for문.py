# for문 기본 구조

# for 변수 in 리스트(또는 튜플, 문자열):
#     수행할 문장1
#     수행할 문장2
#     수행할 문장3
#     . . .

'''
# 전형적인 for문
test_list = ['one', 'two', 'three']
for i in test_list: # 반복문이 돌때마다 test_list안에 있는 0번 index부터 차례대로 i에 입력된다.
    print(i)
'''
'''
# 약간 헷갈리는 for문
a = [(1,2), (3,4), (5,6)] # 리스트 안에 튜플이 있음
for (first, last) in a: # a 리스트 안에 있는 튜플의 값을 각각 정의 하였음
    print("첫 값 : ", first, "마지막 값 : ",last)
'''

'''
# 종합판 for문
marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks: # marks 리스트 안에서 값 하나를 빼는 것을 mark라고 하고 marks의 값이 없으면 종료
    number += 1    # 실행할때 마다 number의 값을 1 더한다.
    if mark >= 60: # marks 안의 mark(index) 값이 60점 이상이면 합격을 출력
        print(f"{number}번 학생은 합격입니다.")
    else:          # 60점 미만이면 불합격을 출력
        print(f"{number}번 학생은 불합격입니다.")
'''

'''
# for문 continue [break도 비슷하게 가능]
marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks: # marks 리스트 안에서 값 하나를 빼는 것을 mark라고 하고 marks의 값이 없으면 종료
    number += 1    # 실행할때 마다 number의 값을 1 더한다.
    if mark < 60: continue # 만약에 mark(index)가 60 이상일 경우 print문 실행하고 아닐 시 continue에 의해 for문 처음으로 이동
    print(f"{number}번 학생은 합격입니다.")
'''

'''
# for와 함께 자주 사용하는 range함수
sum = 0
for i in range(1, 11): # 1이상 11미만의 수를 반복문이 돌때마다 차례대로 i에 담긴다.
    sum += i
    print("sum의 값은", sum, "이고,", "i의 값은", i,"입니다.")
'''

'''
# 이중 for문 : 구구단   =>   debugging 참고
for i in range(2, 10):     # 2~9까지 순차적으로 i에 담겠다. => 아래의 j가 1부터 9까지 다 돌아야 실행
    for j in range(1, 10): # 1~9까지 순차적으로 j에 담겠다.
        print(i*j, end=" ") # end=" " : print문이 끝나면 \n이 되는게 아닌 " " 공백 하나만 생기게 된다.
    print('') # j가 한번 다 돌면 \n 하겠다.
'''


# 리스트 내포(List comprehension) :
'''
# 식 1
a = [1,2,3,4,5]
result = [num * 3 for num in a]  # [num 3] : (3)결과   [for num in a] : (1)for문   [if num % 2==0] : (2)if문
print(result)                    
# num*3 를 담은 result라는 list를 만들고 싶은게 결과 / 여기서 num이란 for문을 돈 결과
# 즉, num*3가 담고 싶은 값이고 그 뒤는 기존 for문을 한줄로 쓰는 형태로 작성하면 됨

a = [1,2,4,3,5]     # 위의 식과 동일
result = []             
for num in a:
    result.append(num*3)
print(result)
'''
'''
# 식 2
a = [1,2,3,4,5]
result = [num*3 for num in a if num % 2==0]  
print(result)                               

a = [1,2,4,3,5]     # 위의 식과 동일
result = []             
for num in a:
    if num % 2==0:
        result.append(num*3)
print(result)
'''
'''
# 식 3
result = [x*y for x in range(2,10) for y in range(1,10)] 
print(result)                               

a = [1,2,4,3,5]     # 위의 식과 동일
result = []             
for x in range(2,10):
    for y in range(1,10):
        result.append(x*y)
print(result)
'''