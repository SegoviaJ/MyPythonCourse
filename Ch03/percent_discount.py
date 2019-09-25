import sys

price = int(sys.argv[1])
percent = int(sys.argv[2])

discount = str(round(price-percent/100*price,2))

print('$'+sys.argv[1]+' at '+sys.argv[2]+'% discount is $'+discount)