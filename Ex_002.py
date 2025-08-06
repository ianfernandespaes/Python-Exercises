name = input("Type your name: ")
print("Nice to meet you! {:=^20}".format(name))

n1 = int(input("Type a number {}: ".format(name)))
n2 = int(input("Type another number: "))
sum = n1 + n2
product = n1 * n2
division = n1 / n2
int_division = n1 // n2
power = n1 ** n2
print("The sum is {}, the product is {} and the division is {:.3f}".format(sum, product, division))
print("The integer division is {}, and the power is {}".format(int_division, power))
