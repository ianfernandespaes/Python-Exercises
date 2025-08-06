name = input("Enter your name: ")
if name == "Gustavo":
    print("What a beautiful name you have!")
elif name == "Pedro" or name == "Maria" or name == "Paulo":
    print("Your name is very popular in Brazil.")
elif name in "Ana Cláudia Jéssica Juliana":
    print("Beautiful feminine name")
else:
    print("Your name is quite common.")
print(f"Have a good day, {name}!")
