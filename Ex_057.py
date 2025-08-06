resp = 'S'
sum_ = quantity = average = largest = smallest = 0
while resp in 'Ss':
    num = int(input('Enter a number: '))
    sum_ += num
    quantity += 1
    if quantity == 1:
        largest = smallest = num
    else:
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num

    resp = str(input('Do you want to continue? [S/N]: ')).upper()
average = sum_ / quantity
print('You entered {} numbers and the average was {:.2f}'.format(quantity, average))
print('The largest value was {} and the smallest value was {}'.format(largest, smallest))
