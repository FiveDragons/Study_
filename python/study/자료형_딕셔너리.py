
# 딕셔너리 : 사전이라고 보면 편하다.
# 사전은 어떤 단어(키)가 있다면 그 뜻(자료구조)이 쭉 나오는 것

# [루비 :Hash], [자바 : Map, Hash_Map], [자바스크립트 : Object], [JSON : Java_Script_Object_Notation] -> 딕셔너리 형태
# API에서 자주 활용된다. 


# 딕셔너리 활용 
# Key와 Value로 이루어져 있다.
# Key를 통해 Value를 얻는다. 
# 딕셔너리의 핵심 : Key를 이용해서 빠르게 찾을 수 있다.

'''
# 딕셔너리에서 Key 사용해 Value 얻기
dic = { 
    "이름" : "캉골",
    "나이" : 25,
    "성별" : "중성",
    "주소" : "자연시 숲구 정글동",
    "특기" : "권투, 사업",
    "가족관계" : {"#" : 2, "아버지" : "캉글", "어머니" : "캉수"},
    "회사" : "캉골골골"
}
print(dic["이름"])      # 딕셔너리를 만들어 놓고 거기서 필요한 자료를 꺼내 쓸 수 있다.
print(dic["가족관계"])
'''

'''
# 딕셔너리 "쌍" 추가하기
a = {1 : 'a'}
a['name'] = "익명"
print(a)

# 딕셔너리 요소 삭제하기
# del a[1] # index로 삭제하는 건 안되고
del a['name'] # key값을 등록해야 삭제가 된다.
print(a)
'''

'''
# 딕셔너리 만들 때 주의할 사항 : value는 겹쳐도 되지만 key가 겹치면 안된다.
a = {1: 'a', 1: 'b'}
print(a[1])                # 출력은 되지만 마지막 밸류만 출력됨
print(a)                   # 중복에 의해 마지막 키와 밸류만 남게된다.
'''

'''
# Key 리스트 만들기(keys)
a = {1: '지갑', 2: '시계', 3: '장갑'}
print(a.keys()) # key값만 뽑아 list와 비슷한(dict_keys) 형태 를 만듦

# Value 리스트 만들기(values)
a = {1: '지갑', 2: '시계', 3: '장갑'}
print(a.values()) # value값만 뽑아 list와 비슷한(dict_values) 형태 를 만듦

# Key, Value 쌍 얻기(items)
a = {1: '지갑', 2: '시계', 3: '장갑'}
print(a.items()) # key와 value 전체를 새로운 배열안에 튜플 형태로 각각 담을 수 있다.

# [keys, values, items] = for문에 자주쓰임 
for k, v in a.items():
    print("키는: " + str(k))
    print("밸류는 : " + v)
'''

'''
# Key:Value 쌍 모두 지우기(clear)
a = {1: '지워질', 2: '키와', 3: '밸류'}
print(a)
a.clear() 
print(a)
'''

'''
# Key로 Value얻기(get)
a = {1: '삼겹살', 2: '항정살', 3: '가브리살'}

print(a.get(1)) # a[1]과 차이가 없어 보이지만
print(a[1])

print(a.get(4)) # a.get()은 없는 Key를 입력했을때 None 이라는 값을 반환해주고
# print(a[4])     # a[]는 없는 Key를 입력했을때 에러를 낸다.

print(a.get(4, '값이 없음')) # 추가로 default값, 4라는 key가 없을 때 '값이 없음'을 리턴해라 라고도 가능하다.

# 해당 Key가 딕셔너리 안에 있는지 조사하기(in)
print(4 in a) # a라는 딕셔너리 안에 4라는 키가 있는지 묻고
print(1 in a) # 없을경우 False / 있을경우 True를 반환한다.
'''