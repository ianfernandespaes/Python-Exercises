count = ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty')
while True:
    num = int(input('Enter a number from 0 to 20: '))
    if 0 <= num <= 20:
        break
    print('Try again. ', end='')
print(f'You entered the number {count[num]}')
