price = float(input("What is the price of the product: R$"))
new_price = price - (price * 10 / 100)
print("The product that costs R${} with a 10% discount will cost R${:.2f}".format(price, new_price))
