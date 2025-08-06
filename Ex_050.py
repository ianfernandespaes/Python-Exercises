sex = str(input("What is your sex? [M/F]: ")).strip().upper()[0]
while sex not in 'MF':
    sex = str(input("Invalid data. Please enter your sex: ")).strip().upper()[0]
print('Sex {} registered successfully!'.format(sex))
