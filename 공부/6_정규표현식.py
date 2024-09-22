#정규표현식
# []는 안에중 한개, [a-c]=abc중 한개, [a-z]:소문자 알파벳 [0-9]:모든숫자, [^]:not을 의미
# \d=숫자, \s=space, \w=문자,숫자, \쓸떄는 r
# a.b에서 '.'은 \n을 제외한 모든 문자중 하나, '.'을 표현하고싶으면[.]으로
# *은0에서무한, +는 하나부터 무한, ?는 없거나 한개, {2}는 2개, {2-5}는 2-5개
# import re-> a=re.compile(r'가려낼 정규표현식')-> a.x(data)
#가능한 x는 .match(처음부터), .search(전체중 1개), .findall(맞는것 리스트로)
# match와 search의 메서드-> .group(), .start(), .end(), .span()
# re.compile(a,re.x)의 x옵션: S:.에\n포함, I:대소문자구별없게끔, M:^,$사용할때 각 줄의 처음이 가능하게끔
# 'a|b':a or b, ^:문자열의 맨처음, $:문자열의 끝, \b:space
# 그루핑(): 정규표현식안에 그루핑가능->하나의 group이 되어 .group(1)이나 \g<1>과 같은 경우로 사용가능
# [abc]{2}:ba등, (abc){2}=abcabc
# 문자열 바꾸기: a=re.compile(x)->a.sub(y,data) : data중 x와 맞는것을 y로 바꾼다

#주민등록증 예시-끝7자리를 #으로
data1='''
조우현 970101-1234567
조경욱 990101-2345678
조엄마 700202-3456789
조아빠 660303-4567890
''' 
import re
a=re.compile(r'(\d{6}-)\d{7}')
result_data1=a.sub(r'\g<1>#######',data1)
print(result_data1)

#전화번호 끝자리를 #으로
data2='''
park 010-9999-9988
kim 010-9909-7789
lee 010-8789-7768
'''
b=re.compile(r'(\d{3}-)(\d{4}-)\d{4}')
result_data2=b.sub(r'\g<1>\g<2>####',data2)
print(result_data2)