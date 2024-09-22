# 300원짜리 커피머신/수령은 총 20개
coffee=20
while True:
     money=int(input('동전을 넣으세요'))
     if money==300:
             coffee=coffee-1
             print('커피를 주고 남은 양은 %s입니다.' %coffee)
     elif money>300:
             coffee=coffee-1
             print(f'커피를 주고 남은 거스름돈은 {money-300}이며 남은 커피양은 {coffee}입니다')
     else:
             print('돈을 반환합니다')
             print('남은 커피양은 %s 입니다.' %coffee)
     if coffee==0:
             '판매를 중지합니다'
             break
