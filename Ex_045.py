a = int(input('Enter a value: '))
b = int(input('Enter another value: '))
c = int(input('Enter one more value: '))
# smallest
smallest = a
if b < a and b < c:
    smallest = b
if c < a and c < b:
    smallest = c
# largest
largest = a
if b > a and b > c:
    largest = b
if c > a and c > b:
    largest = c
print('The smallest value entered was {}'.format(smallest))
print('The largest value entered was {}'.format(largest))
