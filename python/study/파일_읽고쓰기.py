# 파일 읽고 쓰기

'''
# 파일 생성하기
f = open("fileRW.txt", 'w') # f라는 파일을 오픈하고 'fileRW.txt'이라는 파일을 상대주소로 만들고 'w'(Write) 쓰다.
f.close    # 파일을 닫겠다.
'''


# 파일 열기모드     |        설명

#     w(Write)     |     쓰기모드 - 파일에 내용을 쓸 때 사용 (갈아엎기)
#     r(read)      |     읽기모드 - 파일을 읽기만 할 때 사용 (불러오기)
#     a(add)       |     추가모드 - 파일의 마지막에 새로운 내용을 추가 시킬 때 사용 (추가하기)


# 절대주소 : 처음부분(C:/)부터 주소를 써주는 것  (ex => "C:/Python/fileRW.txt")
# 상대주소 : 현재 실행하는 파일을 기준으로 상대적인 경로를 써주는 것 (ex => "fileRW.txt")

'''
# 쓰기모드 : 파일을 쓰기 모드로 열어 출력값 적기
f = open("fileRW.txt", 'w', encoding="UTF-8") # encoding을 통해 한글이 깨지지 않게 해준다.
f.write("파일_읽고쓰기 공부중입니다.\n") # 
for i in range(1, 11):               # 1부터 10까지 for문을 돈다.
    data = f"{i}번째 줄입니다.\n"     # data라는 변수에 i+번째 줄입니다. 라는 값을 넣어준다.
    f.write(data)                    # f변수에 .write이라는 함수를 통해 data의 값을 넣는다.
f.close()                            # 파일을 열었으니 닫는다.
'''

'''
# 읽기모드 : readline()함수 => 파일에 있는 내용을 한 줄씩 읽어오는 함수
f = open("fileRW.txt", 'r', encoding="UTF-8") # read를 통해 값을 읽어온다.
while True:                 # 무한반복 
    line = f.readline()     # fileRW.txt에 있는 내용을 불러올때 사용함
    if not line : break     # 라인이 없다면 (False) break하여라
    print(line)
f.close()                   # 파일을 열고 닫지 않으면 문제가 생길 수 있기에 꼭 닫는다.
'''
'''
# 읽기모드 : readlines()함수 => 파일에 있는 내용을 한줄씩 한번에 다 읽어온다.
f = open("fileRW.txt", 'r', encoding="UTF-8")
lines = f.readlines()     # lines는 fileRW의 내용을 한줄씩 담고있는 list이다.
for line in lines:
    print(line.strip("\n")) # strip() : 양쪽끝에서 특정 문자를 제거해주는 함수
f.close()
'''
'''
# 읽기모드 : read()함수 => readlines와 비슷하게 다 읽어오지만 read는 한번에 읽어온다.
f = open("fileRW.txt", 'r', encoding="UTF-8")
data = f.read() # 통째로 다 읽어온다..
print(data)
f.close()
'''

'''
# 추가모드
f = open("fileRW.txt", 'a', encoding="UTF-8") # add를 통해 값을 추가한다.
for i in range(11, 20):
    data = f"{i}번째 줄입니다.\n"
    f.write(data)
f.close
'''

'''
# with문과 함께 사용하기 / close없이 파일 사용하는 법

with open("fileRW2.txt", "w", encoding="UTF-8") as f: # with을 활용하여 fileRW2.txt에 새로 작성하고 as를 사용해서 변수(f)에 저장한다.
    f.write("파일_읽고쓰기 공부중입니다.") # f는 2번째 줄 까지만 사용되고 3번째 줄 부터 자동으로 close가 되기에 별도의 close가 필요없다.
'''