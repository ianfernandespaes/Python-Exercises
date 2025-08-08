palavras = ['banana', 'maçã', 'laranja', 'uva', 'kiwi', 'manga', 'cabelereiro', 'abacaxi']

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos as vogais: ', end='')
    for letra in p:
        if letra in 'aeiou':
            print(letra, end=' ')