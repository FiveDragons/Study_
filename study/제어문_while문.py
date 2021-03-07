#while문 기본 구조

# while <조건문>:
#     <수행할 문장1>
#     <수행할 문장2>
#     <수행할 문장3>
#     . . .

'''
# 전형적인 while문

treeHit = 0
while treeHit < 10 :        # treeHit가 10보다 작을때 반복해라
    treeHit = treeHit +1    # 1번 실행될때 마다 treeHit에 1을 더해라 / treeHit += 1 와 같은 방식이다.
    # 파이썬에선 treeHit++가 불가능하다. 
    print(f"나무를 {treeHit}번 찍었습니다.")
    if treeHit == 10:       # treeHit가 10이 되었을 경우 실행해라
        print("나무가 넘어갑니다.")
'''

'''
# break : 반복문을 강제로 끝냄
coffee = 10
money = 300
while money: # money가 있을 경우 실행 
    print("돈을 받았으니 커피를 줍니다.")
    coffee -= 1
    print(f"남은 커피의 양은{coffee}개입니다.")
    if not coffee: # coffee가 false가 될 경우 실행
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break # 위의 while식에 money가 True이기에 실행되어야 하지만, break를 이용해 강제로 반복문을 끝내겠다.
'''

'''
# continue : 아래줄을 더 실행 시키지 않고 반복문 맨 윗줄로 올라감 
a = 0
while a < 10: # a가 10보다 작을경우 실행
    a += 1    # 반복될때마다 a에 1을 더해줌
    if a % 2 == 0: # a를 2로 나눈값이 0이라면 (2의 배수) 실행
        continue   # 2의 배수이기에 continue가 실행 되어 아래 print를 실행시키지 않고 while문 처음으로 돌아감
    print(a)
'''

'''
# 무한루프
while True:
    print("안녕하세요")
'''
