#패키지=모듈의 집합             c:/doit/game
# game/                     game=root directory
#     __init__.py           __init__이 각 dir이 패키지임을 알려줌
#     sound/                sound,graphic,play=sub directory
#         __init__.py
#         echo.py
#         wav.py
#     graphic/
#         __init__.py
#         screen.py
#         render.py
#     play/
#         __init__.py
#         run.py
#         test.py

import sys
sys.path.append('c:/doit')      #game이 있는 위치
import game.sound.echo          #항상 .py가 끝에
a=game.sound.echo.echo_test()       #print 'echo'

from game.sound import echo     #이런식으로도 가능
echo.echo_test()



#game의 __init__.py에도 정보넣을수있음
import game
print(game.version)     #3.5기나옴

# or 미리 import도 가능
#from .graphic.render import render_test가 미리 __init__.py에 적혀있음
import game
game.render_test()

# __init__.py에 print문도 있음->import하면 바로 print문 작동->initializing game...

#__init__.py에 __all__=['echo']적혀있음
from game.sound import *        #지정된 'echo'만 불려옴
echo.echo_test()