weight = float(input("What is your weight? "))
height = float(input("What is your height? "))
bmi = weight / (height ** 2)
print("The BMI of this person is {:.1f}".format(bmi))
if bmi < 18.5:
    print("You are under the normal weight")
elif 18.5 <= bmi < 25:
    print("You are in the normal weight range")
elif 25 <= bmi < 30:
    print("You are overweight")
elif 30 <= bmi < 40:
    print("You are obese")
else:
    print("You are morbidly obese")
