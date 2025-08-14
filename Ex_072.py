listanum = []
maior = 0
menor = 0
for i in range(0, 5):
    listanum.append(int(input(f"Digite um valor para a posição {i}: ")))
    if i == 0:
        maior = menor = listanum[0]
    else:
        if listanum[i] > maior:
            maior = listanum[i]
        if listanum[i] < menor:
            menor = listanum[i]
print('+-' * 30)
print(f'Os valores digitados foram: {listanum}')
print(f'O maior valor digitado foi: {maior} nas posições ', end=' ')
for i, v in enumerate(listanum):
    if v == maior:
        print(f'{i}... ', end=' ')
print()
print(f'O menor valor digitado foi: {menor} nas posições ', end=' ')
for i, v in enumerate(listanum):
    if v == menor:
        print(f'{i}... ', end=' ')