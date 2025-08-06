from random import randint
v = 0
while True:
    player = int(input('Enter a value: '))
    computer = randint(0, 10)
    total = player + computer
    choice = ' '
    while choice not in 'PI':
        choice = str(input('Even or Odd [E/O]: ')).strip().upper()[0]
    print(f'You played {player} and the computer {computer}. Total is {total}')
    print('It\'s even') if total % 2 == 0 else print('It\'s odd')
    if choice == 'P':
        if total % 2 == 0:
            print('You won!')
            v += 1
        else:
            print('You lost!')
            break
    elif choice == 'I':
        if total % 2 == 1:
            print('You won!')
            v += 1
        else:
            print('You lost!')
            break
    print('Let\'s play again...')
print(f'Game Over! You won {v} times')
