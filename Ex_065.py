print('=' * 30)
print('{:^30}'.format('Ted Bank'))
print('=' * 30)
amount = int(input('What amount do you want to withdraw? R$'))
total = amount
bill = 50
bill_count = 0
while True:
    if total >= bill:
        total -= bill
        bill_count += 1
    else:
        if bill_count > 0:
            print(f'Total of {bill_count} bills of R$ {bill} reais.')
        if bill == 50:
            bill = 20
        elif bill == 20:
            bill = 10
        elif bill == 10:
            bill = 1
        bill_count = 0
        if total == 0:
            break
print('=' * 30)
print('Come back soon. Have a nice day!')
