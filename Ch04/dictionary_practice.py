squares={
    1:1,
    5:25,
    2:4,
    3:9,
    4:16
    }
print('squares=',squares)

for key,value in squares.items():
    print(f'The square of {key} is {value}')
print()

print('pop(4)=',squares.pop(4))
print('squares=',squares)
print()

squares[6]=36
print('squares added [6]:',squares)
print()

print('squares.popitem() returns:',squares.popitem())
print('squares after popitem:', squares)
print()

del squares[2]
print('squares after del squares[2]',squares)
print()

# del squares[7]

squares.clear()
print('squares after clear:',squares)
del squares

# print(squares)