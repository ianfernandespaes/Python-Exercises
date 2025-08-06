count = 0
sum_ = 0
num = int(input('Enter a number [999 to stop]: '))
while num != 999:
    sum_ += num
    count += 1
    num = int(input('Enter a number [999 to stop]: '))
print('You entered {} numbers and their sum is {}'.format(count, sum_))
