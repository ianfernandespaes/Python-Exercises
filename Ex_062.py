total = tot_over_1000 = cheapest_price = count = 0
cheapest_product = ''
while True:
    product = str(input('Enter the product name: '))
    price = float(input('Price: R$'))
    total += price
    count += 1
    if price > 1000:
        tot_over_1000 += 1
    if count == 1 or price < cheapest_price:
        cheapest_price = price
        cheapest_product = product
    resp = ' '
    while resp not in 'SN':
        resp = input('Do you want to continue? [Y/N] ').strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format('END OF PROGRAM'))
print(f'The total purchase amount was R$ {total:.2f}')
print(f'There are {tot_over_1000} products costing more than R$ 1000.00')
print(f'The cheapest product was {cheapest_product} which costs R$ {cheapest_price:.2f}')
