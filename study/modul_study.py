# modul_study.py
def plus(a,b):
    return a + b

def minus(a,b):
    return a - b



# 내가 실행시키려 하는 파일이 main이라면 실행한다. ( modul_study.py 는 main이기에 실행이됨 )
# import로 파일을 불렀을땐 main이 아닌 파일이름이 돼서 실행이 되지 않음 ( _모듈.py 는 main이 아니기에 실행이 안됨 )
if __name__ == "__main__": 
    print(plus(1,4))
    print(plus(4,2))