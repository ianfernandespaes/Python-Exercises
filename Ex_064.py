num = int(input("Enter a number: "))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print("Analyzing the number {}".format(num))
print("Units: {}".format(u))
print("Tens: {}".format(d))
print("Hundreds: {}".format(c))
print("Thousands: {}".format(m))
