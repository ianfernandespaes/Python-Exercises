from random import randint
num = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('The drawn values were: ', end='')
for n in num:
    print(f'{n} ', end='')
print(f'\nThe highest drawn value was {max(num)}')
print(f'The lowest drawn value was {min(num)}')
