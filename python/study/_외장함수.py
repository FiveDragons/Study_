# 외장함수 : 라이브 러리 함수에서 가져다 import해서 쓰는 것

'''
# sys : 시스템을 다룰때 사용한다.
import sys 
print(sys.argv) # argv를 이용하여 값을 주면 사용할 수 있다.
'''

'''
# pickle : 파일형태로 저장할 수 있는데, 딕셔너리 같은 데이터를 
# pickle을 통해 dump명령어로 저장하게 되면 언제든 딕셔너리 형태로 꺼내와서 쓸 수 있다.

import pickle
f = open("test.txt", 'wb')
data = {1: 'python', 2: 'you need'}
pickle.dump(data, f)
f.close()

import pickle
f = open("test.txt", 'rb')
data = pickle.load(f)
print(data)
'''

'''
# time : 날짜를 출력할때 사용한다.
import time
print(time.time()) # 1970년 1월 1일 0시 0분 0초를 기준으로 지난 시간 초
print(time.localtime(time.time())) # 현재 시간 튜플 출력
'''
'''
# time.sleep : 텀을 줘야할때 사용한다.
#sleep1.py
import time
for i in range(5):
    print(i)
    time.sleep(1) # 1초 텀을 준다.
'''

'''
# random : 난수 생성 (로또번호 생성 등)
import random
lotto = sorted(random.sample(range(1,46), 6)) # 1~45의 수를 랜덤으로 6개 등록하라
print(lotto)
'''

'''
# webbrowser : 웹브라우저를 열때 사용한다.
import webbrowser
webbrowser.open("http://google.com") # 구글 웹브라우저를 열어라
'''

'''
# os :  Operating System의 약자로서 운영체제에서 제공되는 여러 기능을 파이썬에서 수행할 수 있게 해줍니다.
import os

print(os.getcwd()) # 현재 주소 출력

print(os.listdir()) # os.listdir를 사용하면 해당 디렉터리에 있는 파일들의 리스트를 구할 수 있고, 보통 py의 파일, txt을 따로 구분할 경우 사용함

# https://wikidocs.net/3141 참고
'''