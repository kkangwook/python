#a메모장의 탭을 4칸으로 변형시킨것을 b메모장에 적기
import sys

a=sys.argv[1]
f=open(a,'r')
x=f.read()
y=x.replace('\t','    ')
f.close()
b=sys.argv[2]
f=open(b,'w')
f.write(y)
f.close()
