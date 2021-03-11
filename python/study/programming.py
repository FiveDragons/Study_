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
# [4] 간단한 메모장 만들기
# 원하는 메모를 파일에 저장하고 추가 및 조회가 가능한 간단한 메모장을 만들어보자. (programming_study.txt)

# TERMINAL(명령행)에서 작성 : (추가 : python 경로 옵션 "글")(조회 : python 경로 옵션)
#                    ( python .\python\study\programming.py -a "programming study")

import sys # argv를 사용하기 위해 sys를 import한다.

option = sys.argv[1] 
# sys.argv는 프로그램을 실행할 때 입력된 값을 읽어 들일 수 있는 파이썬 라이브러리이다.
# sys.argv[0]는 입력받은 값 중에서 파이썬 프로그램 이름인 programming_study.py이므로 우리가 만들려는 기능에는 필요 없는 값이다.
# 그리고 순서대로 sys.argv[1]은 프로그램 실행 옵션 값이 되고 sys.argv[2]는 메모 내용이 된다.

if option == '-a':     # option이 -a와 같다면 / 쓰기모드(추가)
    memo = sys.argv[2] # memo변수에 [2](메모 내용)의 값을 넣어라
    f = open('programming_study.txt', 'a') # programming_study.txt라는 파일을 열어 'a'[추가]하겠다.
    f.write(memo)   # [2](메모 내용) add하겠다.
    f.write('\n')   # [2](메모 내용)을 추가 한 뒤 한줄 내리겠다.
    f.close()       # 열었던 파일을 닫아준다.
elif option == '-v':   # option이 -v와 같다면 / 읽기모드(조회)
    f = open('programming_study.txt') # programming_study.txt라는 파일을 열겠다.
    memo = f.read() # 메모 내용들을 불러오겠다.
    f.close()       # 열었던 파일을 닫아준다.
    print(memo)     # 불러온 내용을 화면에 보여준다.
'''

'''
# [5] 탭을 4개의 공백으로 바꾸기

# 5번을 풀기위해선 아래의 [1]을 메모장을 미리 입력해놓을것

import sys

src = sys.argv[1] # 입력받는 값 
dst = sys.argv[2] # 출력하는 값

f = open(src)     # [1]src을 열겠다.
tab_content = f.read() # tab_content라는 변수에 쓰겠다.
f.close()         # 열었던 파일을 닫아준다.

space_content = tab_content.replace("\t"," "*4) # \t를 띄어쓰기4개로 교체하여라
print(space_content)

f = open(dst, 'w')     # [2]dst(우리가 생성할 파일)를 읽기 형태로 열겠다.
f.write(space_content) # 교체 했던 값을 읽어온다.
f.close()              # 열었던 파일을 닫아준다.
'''

'''
# [6] 하위 디렉터리 검색하기
# 특정 디렉터리부터 시작해서 그 하위 모든 파일중 파이썬 파일(*.py)만 
# 출력해 주는 프로그램을 만들려면 어떻게 해야 할까?
import os

def search(dirname):
    try: # 오류확인
        filenames = os.listdir(dirname) # os.listdir를 사용하면 해당 디렉터리에 있는 파일들의 리스트를 구할 수 있다.
        for filename in filenames: # 불러온 파일을 하나씩 반복문 돌리겠다.
            full_filename = os.path.join(dirname, filename) #  os 모듈에는 디렉터리와 파일 이름을 이어 주는 os.path.join 함수가 있으므로 이 함수를 사용하면 디렉터리를 포함한 전체 경로를 쉽게 구할 수 있다.
            if os.path.isdir(full_filename):  # full_filename이 디렉터리인지 파일인지 구별하기 위하여 os.path.isdir 함수를 사용하였다.
                search(full_filename)  # 디렉터리일 경우 해당 경로를 입력받아 다시 search 함수를 호출하였다. / 해당 디렉터리의 파일이 디렉터리일 경우 다시 search 함수를 호출해 나가면 (재귀 호출) 해당 디렉터리의 하위 파일을 다시 검색하기 시작하므로 결국 모든 파일들을 검색할 수 있게 된다.
            else:
                ext = os.path.splitext(full_filename)[-1] #os.path.splitext는 파일 이름을 확장자를 기준으로 두 부분으로 나누어 준다.
                if ext == ".py":
                    print(full_filename)
    except PermissionError: # os.listdir를 수행할 때 권한이 없는 디렉터리에 접근하더라도 프로그램이 오류로 종료되지 않고 그냥 수행되도록 하여라
        pass

search("C:/")
'''
'''
# 위 코드와 비슷함

# [하위 디렉터리 검색을 쉽게 해주는 os.walk]
# os.walk를 사용하면 위에서 작성한 코드를 보다 간편하게 만들 수 있다. 
# os.walk는 시작 디렉터리부터 시작하여 그 하위 모든 디렉터리를 차례대로 방문하게 해주는 함수이다.
# 디렉터리와 파일을 검색하는 일반적인 경우라면 os.walk를 사용하도록 하자

import os

for (path, dir, files) in os.walk("c:/"):
    for filename in files:
        ext = os.path.splitext(filename)[-1]
        if ext == '.py':
            print("%s/%s" % (path, filename))



'''
