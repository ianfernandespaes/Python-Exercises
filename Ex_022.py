price = float(input("What is the price of the product? R$"))
print('-' * 10)
print('PAYMENT OPTIONS')
print('[1] - Cash/check payment')
print('[2] - Immediate card payment')
print('[3] - 2 installments on card')
print('[4] - 3 or more installments on card')
print('-' * 10)
option = int(input("Choose an option: "))
if option == 1:
    total = price - (price * 10 / 100)
elif option == 2:
    total = price - (price * 5 / 100)
elif option == 3:
    total = price
    installment = total / 2
    print(f'Your purchase will be split into 2 installments of R${installment:.2f} with no interest')
elif option == 4:
    total = price + (price * 20 / 100)
    num_installments = int(input('How many installments? '))
    installment = total / num_installments
    print(f'Your purchase will be split into {num_installments} installments of R${installment:.2f} with interest')
print(f'The original product price is R${price:.2f} and the final price is R${total:.2f}')
