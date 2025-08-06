num = (int(input('Enter a value: ')),
       int(input('Enter another value: ')),
       int(input('Enter one more value: ')),
       int(input('Enter the last value: ')))
print(f'You entered the values {num}')
print(f'The value 9 appeared {num.count(9)} times')
if 3 in num:
    print(f'The value 3 appeared in position {num.index(3) + 1}')
else:
    print('The value 3 was not entered in any position')
print(f'The even values entered were ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
