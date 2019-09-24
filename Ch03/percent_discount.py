import sys

price = float(sys.argv[1])
percent = float(sys.argv[2])

discount = str(round(price-percent/100*price,2))

print('$'+sys.argv[1]+' at '+sys.argv[2]+'% discount is $'+discount)