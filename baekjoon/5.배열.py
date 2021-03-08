# 문제 : N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.

# 입력 : 첫째 줄에 정수의 개수 N (1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄에는 N개의 정수를 공백으로 구분해서 주어진다. 
# 모든 정수는 -1,000,000보다 크거나 같고, 1,000,000보다 작거나 같은 정수이다.

# 출력 : 첫째 줄에 주어진 정수 N개의 최솟값과 최댓값을 공백으로 구분해 출력한다.

# 풀이
'''
import sys

N = int(sys.stdin.readline())
myList = list(map(int, sys.stdin.readline().split()))

high = 1000000
row = 0

for i in range(N):
    if high > myList[i]:  # high가 myList[i]보다 높다면 실행하라
        high = myList[i]  # high에 가장 큰 숫자가 들어간다.
    if row < myList[i]:   # row가 myList[i]보다 낮다면 실행하라
        row = myList[i]   # row에 가장 작은 숫자가 들어간다.
print(high, row)
'''
# 사람은 배워야 한다는걸 다시 알게해준 문제이다.
# 뭔가 함수를 활용해서 할 수 있을 것 같은데 어떻게 해야하지 고민하다 일단 아는 지식으로 풀어보자 하고 풀어봤는데
# 코드가 너무 길어서 어떤 함수가 있을지 알아보니 min,max가 있었다.
'''
import sys
N = int(sys.stdin.readline())
myList = list(map(int, sys.stdin.readline().split()))
print(min(myList), max(myList))
# 이렇게 짧게 쓸 수 있는 코드인데 당황스럽다. 
# (참고로 여기에서 N은 활약하는것이 없음에도 백준에선 정답으로 표기된다.)
'''






# 문제 : 9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.
# 예를 들어, 서로 다른 9개의 자연수  3, 29, 38, 12, 57, 74, 40, 85, 61
# 이 주어지면, 이들 중 최댓값은 85이고, 이 값은 8번째 수이다.

# 입력 : 첫째 줄부터 아홉 번째 줄까지 한 줄에 하나의 자연수가 주어진다. 주어지는 자연수는 100 보다 작다.

# 출력 : 첫째 줄에 최댓값을 출력하고, 둘째 줄에 최댓값이 몇 번째 수인지를 출력한다.

# 풀이
'''
import sys

arrList = []

for i in range(9):
    arrList.append(int(sys.stdin.readline()))

print(max(arrList))
print(arrList.index(max(arrList))+1)
# 복잡한 느낌이 있지만 아주 간단하다. 
# [1] for문을 이용해 출력문을 9번 작성할 수 있게 만든다.
# [2] 위 문제에서 푼것 처럼 max를 이용하여 arrList의 최대값을 구한다.
# [3] .index를 활용하여 max(arrList)의 최대 index값을 찾아준다.
'''






# 문제 : 세 개의 자연수 A, B, C가 주어질 때 A × B × C를 계산한 결과에 0부터 9까지 각각의 숫자가 몇 번씩 쓰였는지를 구하는 프로그램을 작성하시오.
# 예를 들어 A = 150, B = 266, C = 427 이라면 A × B × C = 150 × 266 × 427 = 17037300 이 되고, 계산한 결과 17037300 에는 0이 3번, 1이 1번, 3이 2번, 7이 2번 쓰였다.

# 입력 : 첫째 줄에 A, 둘째 줄에 B, 셋째 줄에 C가 주어진다. A, B, C는 모두 100보다 같거나 크고, 1,000보다 작은 자연수이다.

# 출력 : 첫째 줄에는 A × B × C의 결과에 0 이 몇 번 쓰였는지 출력한다. 
# 마찬가지로 둘째 줄부터 열 번째 줄까지 A × B × C의 결과에 1부터 9까지의 숫자가 각각 몇 번 쓰였는지 차례로 한 줄에 하나씩 출력한다.

# 풀이
'''
import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())
hapList = list(str(a*b*c)) # 곱한 값이 list형태로 한글자씩 남는다. => ['1', '7', '0', '3', '7', '3', '0', '0']

for i in range(10):
    print(hapList.count(str(i))) # 'hapList' list 안에 0번 index부터 몇개 있는지 차례대로 출력
'''