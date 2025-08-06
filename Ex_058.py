cont = soma = 0
while True:
    num = int(input('Enter a number: '))
    if num == 999:
        break
    cont += 1
    soma += num
print('The sum of the {} numbers entered is {}'.format(cont, soma))
