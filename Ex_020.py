r1 = float(input("First segment: "))
r2 = float(input("Second segment: "))
r3 = float(input("Third segment: "))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("The above segments can form a triangle!", end=" ")
    if r1 == r2 == r3:
        print("The triangle is equilateral!")
    elif r1 != r2 != r3 != r1:
        print("The triangle is scalene!")
    else:
        print("The triangle is isosceles!")
else:
    print("The above segments cannot form a triangle!")
