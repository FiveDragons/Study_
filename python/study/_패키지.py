# 패키지 : 모듈 여러 개를 모아놓은 것


# _패키지.py는  package_study 폴더와 연관되어 있음


'''
# 가상의 package_study패키지 예

# __init__ : 패키지를 표현하는 파이썬 파일  /  3.3버전 이후로는 굳이 안 써도 되지만 예전 버전과의 호환을 위해서 만든다고 함

game/
    __init__.py # 패키지 관련 설정 하는 곳
    sound/
        __init__.py # 패키지 관련 설정 하는 곳
        echo.py
    graphic/
        __init__.py # 패키지 관련 설정 하는 곳
        render.py
'''

'''
# 패키지 안의 함수 실행하는 법 (modul과 똑같다.)

# [1]방법 
import package_study.sound.echo
package_study.sound.echo.echo_test()

# [2]방법
from package_study.sound import echo
echo.echo_test()

# [3]방법
from package_study.sound.echo import echo_test
echo_test()

# [4]방법
from package_study.sound.echo import echo_test as pac # as : import한 값을 pac으로 전환하여 부르겠다.
pac()
'''

'''
# __all__ :

# import * : 모든 것을 불러 와라
# 단, 조건이 있다. 패키지 내에 __init__에서 __all__을 사용하여 __all__ = ['echo'] 를 만들어 주어야 * 안에 echo를 사용할 수 있다.

# 즉, __init__안에 __all__ = ['부르면 호출될 함수들'] 을 입력해 놔야 import * 했을때 호출이 된다.

from package_study.sound import * 
echo.echo_test()
'''

'''
# relative 패키지  :
# C:\Users\admin\Desktop\Git\Study_\study\package_study\graphic 에 설명이 더 되어있음
from package_study.graphic import * 
render.render_test()
'''