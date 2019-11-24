print('안녕하세요! \n')
money = int(input('결제금액을 입력하세요 : '))
menu = {'아메리카노':3000 , '라떼':4100 , '모카라떼':4500}
menu_list = []
print('\n메뉴판')
print(menu)
money_2=money

while True:
    want=input('\n메뉴를 입력하세요 :')

    if want in menu:
        print('{}(을)를 추가 하시겠습니까?\n'.format(want))
        choice = int(input('네:1 아니오:2 나가기:3      >>>'))
        if choice==1:
            if money_2 - menu.get(want)<0:
                print('결제 금액 초과\n')       
                print('주문 내역 :  ' )
                print(menu_list)
                print('거스름돈을 반환합니다.\n')
                a=money_2/10000
                b=(money_2%10000)/1000
                c=(money_2%10000)%1000/100
                d=(money_2%10000)%1000%100/10
                print('거스름돈 = 10000원 : %d장 1000원 : %d장 100원 : %d개 10원 : %d개 \n' %(a,b,c,d))
                print('이용해주셔서 감사합니다.\n안녕히 가세요.')
                break
            money_2 = money_2 - menu.get(want)
            menu_list.append(want)
        if choice==3:
            print('이용해주셔서 감사합니다.\n안녕히 가세요.')
            break
    
    else:
        print('잘못입력하셨습니다.\n')

