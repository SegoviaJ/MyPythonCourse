mult_dict={}
for number in range(1,11):
    mult = number*3
    mult_dict[number]=mult

#calling value using dictionary keys
for x in mult_dict:
    print(x, "multiplied by 3 is",mult_dict[x])
print()

#pulling keys and values from items??
for x,y in mult_dict.items():
    print(f'{x} x 3 = {y}')
print()

#just pulling values wihout keys
for z in mult_dict.values():
    print(z)