base = int(input('Enter an integer value: '))
print('Choose one of the bases for conversion:')
print('[ 1 ] Convert to BINARY')
print('[ 2 ] Convert to OCTAL')
print('[ 3 ] Convert to HEXADECIMAL')
option = int(input('Your option: '))
if option == 1:
    print('{} converted to BINARY is {}'.format(base, bin(base)[2:]))
elif option == 2:
    print('{} converted to OCTAL is {}'.format(base, oct(base)[2:]))
elif option == 3:
    print('{} converted to HEXADECIMAL is {}'.format(base, hex(base)[2:]))
else:
    print('Invalid option')
