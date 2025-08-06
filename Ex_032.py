from math import hypot
Num1 = float(input("Length of the opposite side: "))
Num2 = float(input("Length of the adjacent side: "))
hi = hypot(Num1, Num2)
print("The length of the hypotenuse is {:.2f}".format(hi))
