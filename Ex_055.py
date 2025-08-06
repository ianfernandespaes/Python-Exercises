print('PA Generator')
print('-=' * 10)
first_term = int(input('Enter the first term: '))
ratio = int(input('Enter the ratio: '))
term = first_term
count = 1
total = 0
more = 10
while more != 0:
    total = total + more
    while count <= total:
        print('{} -> '.format(term), end='')
        term += ratio
        count += 1
    print('Pause')
    more = int(input('Enter how many more terms you want: '))
print('End')
