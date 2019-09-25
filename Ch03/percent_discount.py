import sys

price = int(sys.argv[1])
percent = int(sys.argv[2])

discount = round(price-percent/100*price,2)


discount = str(discount)
price=str(price)
percent=str(percent)
print('$'+price+' at '+percent+'% discount is $'+discount)