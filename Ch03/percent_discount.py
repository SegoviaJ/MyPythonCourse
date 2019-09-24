import sys

price = float(sys.argv[1])
percent = float(sys.argv[2])

discount = round(price-percent/100*price,2)
discount = str(discount)

print('$'+sys.argv[1]+' at '+sys.argv[2]+'% discount is $'+discount)