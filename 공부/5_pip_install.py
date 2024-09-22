#pip list->설치한 패키지 목록을 출력
#터미널에 pip install X
#pypi.org들어가서 사용법보기
#pip install sympy


#2차 방정식 해 구하기
import sympy
x=sympy.symbols('x')
f=sympy.Eq(x**2,-3)     # x^2=-3인 x값
a=sympy.solve(f)
print(a)

#연립방정식 해 구하기
import sympy
x,y=sympy.symbols('x y')
f1=sympy.Eq(x+y,17)
f2=sympy.Eq(x-y,6)
a=sympy.solve([f1, f2])
print(a)