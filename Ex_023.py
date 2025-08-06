from random import randint
from time import sleep
items = ('Rock', 'Paper', 'Scissors')
computer = randint(0, 2)
print('''Your options:
[ 0 ] ROCK
[ 1 ] PAPER
[ 2 ] SCISSORS''')
player = int(input('What is your move? '))
print('RO')
sleep(1)
print('SHAM')
sleep(1)
print('BO!!!')
print('=-' * 10)
print('The computer chose {}'.format(items[computer]))
print('The player chose {}'.format(items[player]))
print('=-' * 10)

if computer == 0:
    if player == 0:
        print('DRAW')
    elif player == 1:
        print('PLAYER WINS')
    elif player == 2:
        print('COMPUTER WINS')
    else:
        print('INVALID MOVE')
elif computer == 1:
    if player == 0:
        print('COMPUTER WINS')
    elif player == 1:
        print('DRAW')
    elif player == 2:
        print('PLAYER WINS')
    else:
        print('INVALID MOVE')
elif computer == 2:
    if player == 0:
        print('PLAYER WINS')
    elif player == 1:
        print('COMPUTER WINS')
    elif player == 2:
        print('DRAW')
    else:
        print('INVALID MOVE')
