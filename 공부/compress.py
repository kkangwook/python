#문자가 연속적으로 반복되는 경우, 그 반복횟수를 표시해 문자열을 압축하여 표시하는 함수
#ex) aaabbcccccca->a3b2c6a1
def x(a):
    y=''
    b=0
    c=''
    for i in a:
        if i!=y:
            y=i
            if b:
                c+=str(b)
            c+=i
            b=1
        else:
            b+=1
    if b:
        c+=str(b)
    return c
print(x('aaabbcccccca'))