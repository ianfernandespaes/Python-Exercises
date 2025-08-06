width = float(input("Enter the width of the wall: "))
height = float(input("Enter the height of the wall: "))
area = width * height
print("Your wall has the dimensions of {}x{} and its area is {}m²".format(width, height, area))
paint = area / 2
print("To paint this wall you need {}L of paint".format(paint))
