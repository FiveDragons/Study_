# 지금 배운 내용으로 어떤 프로그램을 만들지 감이 오지 않기에 간단한 프로그램을 만들어 보겠다.



# [1] 구구단

# 구구단 프로그램(함수) 만들기
# -n 입력하면 n단 출력
'''
# for문 활용
def GuGu(n):
    result = []
    for i in range(1,10):
        result.append(n*i)
    return result
print(GuGu(5))
'''
'''
# while문 활용
def GuGu(n):
    result = []
    i = 1
    while i < 10:
        result.append(n*i)
        i += 1
    return result
print(GuGu(3))
'''

'''
# [2] 3과 5의 배수 합하기
# 10미만의 자연수에서 3과 5의 배수를 구하면 3,5,6,9이다. 이들의 총합은 23이다.
# 1000미만의 자연수에서 3의 배수와 5의 배수의 총합을 구하라.

result = 0
for n in range(1,1000):
    if n%3 == 0 or n%5 == 0: # 3과 5의 배수 둘중 하나만 나오면 되기 때문에 
        result += n          # 3 or 5을 사용하여 둘 다 맞아도 한번만 출력되는 형식으로 입력하였음
    
print(result)
'''

'''
# [3] 게시판 페이징하기
# 게시물의 총 건수와 한 페이지에 보여줄 게시물 수(n)를 입력으로 주었을 때 총 페이지 수(m)를 출력하는 프로그램

def getTotalPage(m,n):
    if m % n == 0:
        return m//n
    else:
        return m//n + 1

print(getTotalPage(5,10))
print(getTotalPage(15,10))
print(getTotalPage(25,10))
print(getTotalPage(30,10))
'''

'''
# [ 이해 못함 ] 
# [4] 간단한 메모장 만들기
# 원하는 메모를 파일에 저장하고 추가 및 조회가 가능한 간단한 메모장을 만들어보자.


import sys

option = sys.argv[1]

if option == '-a':     # 쓰기모드
    memo = sys.argv[2]
    f = open('memo.txt', 'a')
    f.write('\n')
    f.close()
elif option == '-v':   # 읽기모드
    f = open('memo.txt')
    memo = f.read()
    f.close()
    print(memo)
'''

'''
# [ 이해 못함 ] 
# [5] 탭을 4개의 공백으로 바꾸기
import sys

src = sys.argv[1]
dst = sys.argv[2]

f = open(src)
tab_content = f.read()
f.close()

space_content = tab_content.replace("\t"," "*4)

f = open(dst, 'w')
f.write(space_content)
f.close()
'''

'''
# [6] 하위 디렉터리 검색하기
# 특정 디렉터리부터 시작해서 그 하위 모든 파일중 파이썬 파일(*.py)만 
# 출력해 주는 프로그램을 만들려면 어떻게 해야 할까?
import os

def search(dirname):
    try:
        filenames = os.listdir(dirname)
        for filename in filenames:
            full_filename = os.path.join(dirname, filename)
            if os.path.isdir(full_filename):
                search(full_filename)
            else:
                ext = os.path.splitext(full_filename)[-1]
                if ext == ".py":
                    print(full_filename)
    except PermissionError:
        pass

search("C:/")
'''
