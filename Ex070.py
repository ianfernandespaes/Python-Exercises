listagem = ('lapis', 1.75,
            'borracha', 2.00,
            'caderno', 15.90,
            'estojo', 25.00,
            'transferidor', 4.20,
            'compasso', 9.99,
            'mochila', 120.32,
            'caneta', 3.50,
            'livro', 34.90)
print('-' * 57)
print(f'{"LISTAGEM DE PRODUTOS":^57}')
print('-' * 57)
for item in range(0, len(listagem)):
    if item % 2 == 0:
        print(f"Produto: {listagem[item]:.<30}" , end=' ')
    else:
        print(f"Preço: R$ {listagem[item]:>7.2f}",)