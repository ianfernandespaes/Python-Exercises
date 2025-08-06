print('PA Generator')
print('-=' * 10)
first_term = int(input('Enter the first term: '))
ratio = int(input('Enter the ratio: '))
term = first_term
count = 1
while count <= 10:
    print('{} -> '.format(term), end='')
    term += ratio
    count += 1
print('End')
