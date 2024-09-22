#첫째항이 0, 두번때항이 1일때의 피보나치수열
def x(a):
    b=0
    c=1
    d=0
    if a==1:
        print(b)
    elif a==2:
        print(b,c)
    else:
        print(b,c,end="")
        for i in range(a-2):
            d=b+c
            b=c
            c=d
            print('',d,end='')
            
