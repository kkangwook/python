#해당 디렉토리의 .py파일만 뽑기
import os

def x(a):
    file=os.listdir(a)
    for i in file:
        full_file=os.path.join(a,i)
        ext=os.path.splitext(full_file)[-1]
        if ext=='.py':
            print(full_file)
x('c:/doit')
