grade1 = float(input("Enter the first grade: "))
grade2 = float(input("Enter the second grade: "))
average = (grade1 + grade2) / 2
print("Getting {} and {}, the average grade is: {:.1f}".format(grade1, grade2, average))
if average >= 7:
    print("Approved")
elif average >= 5:
    print("Recovery")
else:
    print("Failed")
