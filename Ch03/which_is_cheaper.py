import math
product1_price = input("What is the price of product 1? ")

print('the type is', type(product1_price))

price1=float(product1_price)

print('product1_price is: ', price1)

print('Product 1 is an interger: ',price1.is_integer())

weight1=float(input("How many ounces is product 1? "))

price2=float(input("What is the price of product 2? "))

weight2=float(input("How many ounces ir product 2? "))

# print(weight1,weight2,price1,price2)

price_per_ounce1=price1/weight1
price_per_ounce2=price2/weight2
print("Price per ounce of product 1:")
print(price_per_ounce1)
print("Price per ounce of product 2:")
print(price_per_ounce2)

print("Product 1 is cheaper:")
print(price_per_ounce1<price_per_ounce2)

print("Product 2 is cheaper:")
print(price_per_ounce1>price_per_ounce2)

print("Are the equal?")
print(price1==price2)
print("")

product_total=price2+price1
print("Total for 1 and 2: ")
print(product_total)

print("Discount amount:")
discount=product_total*.10
print(discount)

print("Final amount:")
print(product_total-discount)
print("")

print("The truncated value of product 1 is",math.trunc(price1))
print("The rounded value of product 1 is",round(price1))
print("The floor value of product 1 is",math.floor(price1))
print("The ceiling value of product 1 is",math.ceil(price1))


