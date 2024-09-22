#홀수가 연속되면 두 수 사이에 '-', 
# 짝수가 연속되면 '*'를 추가하는 함수
def x(a):
    b=str(a)
    c=''
    for i in range(len(b)-1):
        if int(b[i])%2==0 and int(b[i+1])%2==0:
            c=c+b[i]+'*'
        elif int(b[i])%2!=0 and int(b[i+1])%2!=0:
            c=c+b[i]+'-'
        else:
            c=c+b[i]
    c=c+b[len(b)-1]
    print(c)
