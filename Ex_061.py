tot18 = totMales = totFemUnder20 = 0
while True:
    age = int(input('Age: '))
    sex = ' '
    while sex not in 'MF':
        sex = str(input('Sex: [M/F]: ')).strip().upper()[0]
    if age >= 18:
        tot18 += 1
    if sex == 'M':
        totMales += 1
    if sex == 'F' and age < 20:
        totFemUnder20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Do you want to continue? [Y/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total of {tot18} people over 18 years old')
print(f'There are {totMales} males registered')
print(f'And there are {totFemUnder20} females under 20 years old')
