salary = float(input("What is the employee's salary? R$"))
new_salary = salary + (salary * 15 / 100)
print("The salary is R${:.2f} and with a 15% raise will be R${:.2f}".format(salary, new_salary))
