house = float(input('What is the value of the house? R$ '))
salary = float(input("What is the buyer's salary? R$ "))
years = int(input('How many years of financing? '))
installment = house / (years * 12)
minimum = salary * 0.3
print('To pay for a house of R$ {:.2f} in {} years'.format(house, years), end='')
print(' the installment will be R$ {:.2f}'.format(installment))
if installment <= minimum:
    print('Loan can be APPROVED!')
else:
    print('Loan DENIED!')
