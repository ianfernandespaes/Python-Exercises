from time import sleep

n1 = int(input('First number: '))
n2 = int(input('Second number: '))
option = 0
while option != 5:
    print('''
    [ 1 ] add
    [ 2 ] multiply
    [ 3 ] greater
    [ 4 ] new numbers
    [ 5 ] exit the program
    ''')
    option = int(input('What is your option? '))
    if option == 1:
        sum_ = n1 + n2
        print('The sum of {} and {} is {}'.format(n1, n2, sum_))
    elif option == 2:
        multiply = n1 * n2
        print('The multiplication of {} and {} is {}'.format(n1, n2, multiply))
    elif option == 3:
        if n1 > n2:
            greater = n1
            print('The greater number between {} and {} is {}'.format(n1, n2, greater))
        elif n2 > n1:
            greater = n2
            print('The greater number between {} and {} is {}'.format(n1, n2, greater))
        else:
            print('The numbers are equal')
    elif option == 4:
        print('Enter the numbers again')
        n1 = int(input('First number: '))
        n2 = int(input('Second number: '))
    elif option == 5:
        print('Exiting the program...')
    else:
        print('Invalid option, try again')
    print('=-=' * 10)
    sleep(2)
print('End of program! Come back soon!')
