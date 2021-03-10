# render.py

# ..을 통해 package_study로 나가고 sound.echo를 이용해 사운드 안에있는 echo.py에 있는 echo_test를 import를 하겠다.
from ..sound.echo import echo_test  

def render_test():
    print("render")
    echo_test()

# 여기서 실행을 하게 되면 attempted relative import with no known parent package 와 같은 에러가 나는데
# 원인은 python interpreter는  relative import의 module 위치를 정할 때 
# 즉, 기준이 되는 모듈의 위치를 정할 때 __name__속성에 의해 결정된다.
# 터미널에서 직접 python 파일을 실행시킬 때 __name__ == '__main__' 이 된다.
# 그러면 당연히 __main__이라는 모듈의 위치를 파이썬 interpreter는 알 수가 없기 때문에 에러가 발생한다.