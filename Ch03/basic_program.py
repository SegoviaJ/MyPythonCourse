keep_looping=True

while keep_looping:
    month=int(input("Enter a month: "))
    day=int(input("Enter a day: "))

    if (month>0 and month<13 and day>0 and day<=31):
        keep_looping=False
    else:
        print('Invalid. Use 1-12 for month and 1-31 for day')

message=f'Hey. You did it. {month}/{day}.'

print(message)