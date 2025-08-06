from datetime import date
current_year = date.today().year
birth_year = int(input('Year of birth: '))
age = current_year - birth_year
print('Who was born in {} is {} years old in {}.'.format(birth_year, age, current_year))
if age < 18:
    print('There are still {} years left until enlistment.'.format(18 - age))
    print('Your enlistment will be in {}.'.format(current_year + (18 - age)))
elif age > 18:
    print('You should have enlisted {} years ago.'.format(age - 18))
    print('Your enlistment was in {}.'.format(current_year - (age - 18)))
else:
    print('You must enlist IMMEDIATELY!')
