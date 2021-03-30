#IF STATEMENTS

house_price = float(1000000)
good_credit = True

if good_credit:
    down_payment = house_price * 0.1
    print(f'You need to put down ${down_payment}')
else:
    down_payment = house_price * 0.20
    print(f'You need to put down ${down_payment}')