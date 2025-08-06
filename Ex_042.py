speed = float(input('What is the current speed of the car? '))
if speed > 80:
    print('Fined! You exceeded the speed limit of 80km/h')
    fine = (speed - 80) * 7
    print('Your fine is R$ {:.2f}'.format(fine))
print('Have a good day! Drive safely!')
