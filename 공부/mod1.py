def add(a,b):
    return a+b
def sub(a,b):
    return a-b

pi=3.141592
class math:
    def __init__(self,r):
        self.r=r
    def solv(self):
        return pi*(self.r)**2
    
if __name__=='__main__': #이거 없이 import하면 맨 첫결과에 11이 다른 모듈실행에 뜸
    print(add(1,10))