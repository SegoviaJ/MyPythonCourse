def add_numbers(*numbers):
    total=0
    for value in numbers:
        total+=value
    return total

print(add_numbers(4,6,8,6500,65,7,21))
