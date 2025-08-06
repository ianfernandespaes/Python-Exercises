salary = float(input("What is the employee's salary? R$"))
if salary <= 1250:
    new_salary = salary + (salary * 0.15)
else:
    new_salary = salary + (salary * 0.10)
print('Someone who was earning R${:.2f} will now earn R${:.2f}'.format(salary, new_salary))
