import sys

try:
    arg_string1=sys.argv[1]
    arg_string2=sys.argv[2]
except IndexError:
    print('Invalid input. Please enter two whole number values.')
    sys.exit(-1)

try:
    arg1=int(arg_string1)
    arg2=int(arg_string2)
except ValueError as message:
    print('Invalid input:',message)
    sys.exit(-1)
    
total=arg1+arg2

print(total)