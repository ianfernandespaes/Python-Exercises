distance = float(input('What is the distance of your trip? '))
print('You are about to start a trip of {}km'.format(distance))
if distance <= 200:
    price = distance * 0.50
else:
    price = distance * 0.45
print('The price of your trip will be R${:.2f}'.format(price))
