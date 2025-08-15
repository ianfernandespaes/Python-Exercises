numeros = list()
while True:
    n = int(input("Digite um número: "))
    if n not in numeros:
        numeros.append(n)
        print("Número adicionado com sucesso.")
    else:
        print("Número já existe na lista.")
    r = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if r == "N":
        break
print('+-' * 30)
numeros.sort()
print(f"Valores Digitados: {numeros}")