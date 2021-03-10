# 모듈 : 미리 만들어 놓은 .py(파이썬) 파일
# 함수, 변수, 클래스을 하나의 파이썬 파일에 만들어놓고 모듈을 이용하여 가져다 쓰겠다 라는 말


'''
# 사용법
# 모듈을 사용하기 위해 modul_study.py 를 만들어 놓았다.
import modul_study  # modul_study을 import함으로써 그 안에 있는 것을 사용할 수 있음
print(modul_study.plus(1,2)) # modul_study안에 있는 plus라는 함수를 실행하겠다.
print(modul_study.minus(1,2)) # modul_study안에 있는 minus라는 함수를 실행하겠다.
'''

'''
# import 속도 향상 방법 
# 내가 만약 modul_study의 함수중 plus만 쓰고 싶다면 굳이 minus까지 import할 이유가 없으니 plus만 import하여 속도를 높힌다.
from modul_study import minus
print(minus(1,2))   # 특정 함수만 import하면 하나의 함수만 쓰겠다는 뜻이니 "modul_study." 을 하지 않아도 된다.
'''

'''
# modul_study.py에 가면 설명 있음
if __name__ == "__main__": 
    print(plus(1,4))
    print(plus(4,2))
'''


# sys.path.append

# _모듈.py와 modul_study.py의 경로는 study폴더 안에서 같이 있어서 import가 가능하지만
# modul_sudy_folder 폴더에 있는 modul_study_file.py는 같은 경로가 아니기 때문에 import할 수 없다.
# 그렇기에 path에 추가를 하여 경로를 import 할 수 있게 만들어 준다.
import sys
sys.path.append("C:\\Users\\admin\\Desktop\\Git\\Study_\\modul_study_folder") # sys.path.append 를 이용하여 modul_sudy_folder에 있는 파일도 import가능하게 한 뒤

import modul_study_file # modul_study_file을 import하여
print(modul_study_file.plus(3,4)) # modul_study_file안에 plus 함수를 사용하였다.


'''
#__pycache__ : 
# 모듈 로딩을 빠르게 하려고, 파이썬은 __pycache__ 디렉터리에 각 모듈의 컴파일된 버전을 module.version.pyc라는 이름으로 캐싱합니다.
# version은 컴파일된 파일의 형식을 지정합니다. 일반적으로 파이썬의 버전 번호를 포함합니다.
# 작업한 파일을 예로 들면, CPython 배포 3.9 에서 modul_study_file.py의 컴파일된 버전은 __pycache__/modul_study_file.cpyhon-39.pyc로 캐싱 됩니다.
# 이 명명법은 서로 다른 파이썬 배포와 버전의 컴파일된 모듈들이 공존할 수 있도록 합니다.
'''