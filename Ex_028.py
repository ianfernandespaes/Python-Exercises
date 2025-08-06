sum = 0
count = 0
for c in range(1, 7):
    num = int(input('Enter the {}º number: '.format(c)))
    if num % 2 == 0:
        sum += num
        count += 1
print('You entered {} even numbers and their sum is {}'.format(count, sum))
