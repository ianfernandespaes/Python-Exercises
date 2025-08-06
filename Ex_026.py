sum = 0
count = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        sum = sum + c
        count = count + 1
print(f'The sum of all {count} odd numbers that are multiples of three between 1 and 500 is {sum}')
