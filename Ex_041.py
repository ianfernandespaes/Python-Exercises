import time
from random import randint
from time import sleep

computer = randint(0, 5)
print('-=-' * 12)
print("I'm going to think of a number between 0 and 5")
print('-=-' * 12)
player = int(input('Which number did I think of? '))
print('PROCESSING...')
sleep(3)
if player == computer:
    print('Congratulations, you WON!')
else:
    print('You LOST! I thought of the number {} not {}'.format(computer, player))
