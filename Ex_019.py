from datetime import date
current_year = date.today().year
birth_year = int(input('Enter the year of birth: '))
age = current_year - birth_year
print(f'The athlete is {age} years old')

if age <= 9:
    print('Child')
elif age <= 14:
    print('Infant')
elif age <= 19:
    print('Junior')
elif age <= 25:
    print('Senior')
