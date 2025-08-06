tot = 0
num = int(input("Enter a number: "))
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print(c, end=' ')
print('The number {} was divisible {} times'.format(num, tot))
