def print_stars(count=10):
    print('*'*count)

print_stars()
print_stars(20)

def slice_list(list_value,int_value):
    """returns slice if int is valid"""
    if (len(list_value)>int_value):
        print('Slicing..')
        return list_value[:int_value]
    else:
        print('Value too high...',int_value)
        return None

some_nums=[2,6,4,2,22,54,12,8,-1]

print('value returned',slice_list(some_nums,4))
print('value returned',slice_list(some_nums,8))
print('value returned',slice_list(some_nums,12))