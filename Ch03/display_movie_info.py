import sys

program_name=sys.argv[0]

print('original name\t\t',program_name)
print('uppercase\t\t',program_name.upper())
print('original name\t\t',program_name)
program_name=program_name.replace('_',' ')
print('replace_\t\t',program_name)
program_name=program_name.replace('.\\','')
print('remove .\\\t\t',program_name)
program_name=program_name.replace('.py','')
print('remove .py\t\t',program_name)
program_name=program_name.upper()
print('UPPER\t\t\t',program_name)
print()
welcome_message='Welcome to {}'
welcome_message=welcome_message.format(program_name)
print(welcome_message)
print()
print('length is', len(program_name))
welcome_message=welcome_message.center(len(welcome_message)*3,'*')
print(welcome_message)
print()
good_year=False
while not good_year:
    year=input("What year is your favorite movie from? ")
    if(year.isdecimal()):
        good_year=True
    else:
        print("Please enter a valid year")

movie=input("What is your favorite movie? ")
movie=movie.strip()

message="In {}, the movie {} debuted"
print(message.format(year,movie))
print()